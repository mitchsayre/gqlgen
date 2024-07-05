import { PluginFunction, PluginValidateFn, Types, isComplexPluginOutput } from "@graphql-codegen/plugin-helpers";
import { GraphQLSchema, OperationDefinitionNode } from "graphql";
import { GraphQLInput, GraphQLSourceData } from "quicktype-graphql-input";

/**
 * @description This is where we will define options the user can pass to our plugin. Like here: https://the-guild.dev/graphql/codegen/docs/custom-codegen/plugin-structure#add-plugin-configuration.
 */

export interface GqlgenEntrypointConfig {
  language: string; // Add the language property to the config interface
  introspectionResultJson: any;
  namespace: string;
}

export const plugin: PluginFunction<GqlgenEntrypointConfig> = async (
  schema: GraphQLSchema,
  documents,
  config,
  info
): Promise<string> => {
  const sources: GraphQLSourceData[] = documents.map(document => {
    const operationDefinition = document.document?.definitions.find(
      def => def.kind === "OperationDefinition"
    ) as OperationDefinitionNode;
    const operationName = operationDefinition.name?.value!;

    return {
      name: operationName,
      query: document.rawSDL!,
      schema: config.introspectionResultJson,
    };
  });
  // console.log(sources);

  // Import for Python
  const generatePyImports = (sources: GraphQLSourceData[]) => {
    return sources
      .map(source => {
        return `from ${source.name
          .split(/\.?(?=[A-Z])/)
          .join("_")
          .toLowerCase()} import ${source.name}`;
      })
      .join("\n");
  };

  // Import for TypeScript
  const generateTsImports = (sources: GraphQLSourceData[]) => {
    return sources
      .map(source => {
        return `import { Convert as Convert${source.name}, ${source.name} } from './${source.name}.ts'`;
      })
      .join("\n");
  };
  // console.log(generateTsImports(sources));

  // Import for C++
  const generateCppImports = (sources: GraphQLSourceData[]) => {
    return sources
      .map(source => {
        return `#include <${source.name}.h>`;
      })
      .join("\n");
  };

  const queryFormat = (query: string) => {
    return query.split("\n").join(" ");
  };

  // Python operations
  const generatePyOperations = (sources: GraphQLSourceData[]) => {
    return sources
      .map(source => {
        return `
  def ${source.name
    .split(/\.?(?=[A-Z])/)
    .join("_")
    .toLowerCase()}(self, input) -> ${source.name}:
    res = self.execute_operation(
      self,
      input,
      "${source.name}",
      '${queryFormat(source.query)}'
    )
    return ${source.name}.from_dict(res)`;
      })
      .join("\n");
  };

  // TypeScript operations
  const generateTsOperations = (sources: GraphQLSourceData[]) => {
    return sources
      .map(source => {
        return `
  public async ${source.name.charAt(0).toLowerCase()}${source.name.slice(1)}(input: OperationInput): Promise<${
          source.name
        }> {
    const res = await this.executeOperation(
      input,
      "${source.name}",
      '${queryFormat(source.query)}'
    );
    return Convert${source.name}.to${source.name}(res);
  }`;
      })
      .join("\n");
  };
  // console.log(generateTsOperations(sources));

  // C++ operations
  const generateCppOperation = (sources: GraphQLSourceData[]) => {
    return sources
      .map(source => {
        return `
  ${config.namespace}::${source.name}(const Json::Value &input) {
    Json::Value res = executeOperation(
      input,
      "${source.name}",
      R"${queryFormat(source.query)}"
    );
  }`;
      })
      .join("\n");
  };

  // console.log(config.language);
  if (config.language === "Python") {
    return `import requests, json
${generatePyImports(sources)}

class GqlgenClient:
  def __init__(self, config):
    self.config = config

  def execute_operation(self, input, operation_name, document):
    url = self.config.url
    headers = self.config.headers
    body = {
        "query": document,
        "operationName": operation_name,
        "variables": input,
    }

    res = requests.post(url, headers=headers, data=json.dumps(body))
    return res.json()
  ${generatePyOperations(sources)}`;
  } else if (config.language === "TypeScript") {
    return `${generateTsImports(sources)}

type Config = {
  url: string;
  headers: { [key: string]: string };
}

type OperationInput = {
  [key: string]: any;
}

export class GqlgenClient {
  private config: Config;

  constructor(config: Config) {
    this.config = config;
  }

  private async executeOperation(input: OperationInput, operationName: string, document: string): Promise<any> {
    const url = this.config.url;
    const headers = this.config.headers;
    const body = {
      query: document,
      operationName: operationName,
      variables: input,
    };

    const res = await fetch(url, {
      method: "POST",
      headers: {
        ...headers,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    return res.json();
  }
  ${generateTsOperations(sources)}
}`;
  } else if (config.language == "CPlusPlus") {
    return `${generateCppImports(sources)}
#include <iostream>
#include <string>
#include <map>
#include <nlohmann/json.hpp>
#include <httplib.h>
#include <json/json.h>
#pragma once
using namespace std;

struct Config
{
  string url;
  map<string, string> headers;
};

class GqlgenClient
{
private:
  Config config;

public:
  // constructor
  GqlgenClient(const Config &config) : config(config) {}

  Json::Value executeOperation(const Json::Value &input, const string &operationName, const string &document)
  {
    httplib::Client client(config.url.c_str());
    Json::Value body;
    body["query"] = document;
    body["operationName"] = operationName;
    body["variables"] = input;

    Json::StreamWriterBuilder writer;
    string bodyStr = Json::writeString(writer, body);

    httplib::Headers httplibHeaders;
    for (const auto &header : headers)
    {
      httplibHeaders.emplace(header.first, header.second);
    }

    auto res = client.Post("/", httplibHeaders, bodyStr, "application/json");

    Json::Value response;

    if (res && res->status == 200)
    {
      Json::CharReaderBuilder reader;
      string errors;
      istringstream is(res->body);
      string doc = is.str();
      istringstream docStream(doc);
      Json::parseFromStream(reader, docStream, &response, &errors);
    }
    else
    {
      cout << "Error: " << res.error() << endl;
      return Json::Value(); // empty response
    }

    return response;
  }
  ${generateCppOperation(sources)}
  }
  `;
  } else {
    return `Error: Unsupported ${config.language}`;
  }
};

export const validate: PluginValidateFn<any> = async (
  schema: GraphQLSchema,
  documents: Types.DocumentFile[],
  config: GqlgenEntrypointConfig,
  outputFile: string,
  allPlugins: Types.ConfiguredPlugin[]
) => {
  // We can validate the conditions that our plugin needs here and throw errors if necessary.
};
