import { PluginFunction, PluginValidateFn, Types, isComplexPluginOutput } from "@graphql-codegen/plugin-helpers";
import { GraphQLSchema, OperationDefinitionNode } from "graphql";
import { GraphQLInput, GraphQLSourceData } from "quicktype-graphql-input";

/**
 * @description This is where we will define options the user can pass to our plugin. Like here: https://the-guild.dev/graphql/codegen/docs/custom-codegen/plugin-structure#add-plugin-configuration.
 */

export interface GqlgenEntrypointConfig {
  language: string; // Add the language property to the config interface
  introspectionResultJson: any;
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

  const generateImports = (sources: GraphQLSourceData[]) => {
    return sources
      .map(source => {
        return `from ${source.name
          .split(/\.?(?=[A-Z])/)
          .join("_")
          .toLowerCase()} import ${source.name}`;
      })
      .join("\n");
  };
  // console.log(generateImports(sources));

  const queryFormat = (query: string) => {
    return query.split("\n").join(" ");
  };
  const GenerateOperations = (sources: GraphQLSourceData[]) => {
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

  return `import requests, json
${generateImports(sources)}

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
  ${GenerateOperations(sources)}`;
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
