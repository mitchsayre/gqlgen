import * as fs from "fs";
import { TypeScriptTargetLanguageGQL } from "./language/TypeScript.js";

import {
  quicktype,
  InputData,
  JSONSchemaInput,
  CSharpTargetLanguage,
  TypeScriptTargetLanguage,
  cSharpOptions,
  CSharpRenderer,
  RenderContext,
  getOptionValues,
  Sourcelike,
  ClassType,
  Type,
  TypeAttributeKind,
  JSONSchema,
  Ref,
  JSONSchemaType,
  JSONSchemaAttributes,
  ClassProperty,
  Name,
  languageNamed,
  SerializedRenderResult,
  PythonTargetLanguage,
} from "quicktype-core";
import { GraphQLInput, GraphQLSourceData } from "quicktype-graphql-input";
import { PythonTargetLanguageGQL } from "./language/Python.js";
import { targetLanguages } from "./language/index.js";
// import { makeQuicktypeOptions, CLIOptions } from "quicktype";
import fetch from "node-fetch";
import { getIntrospectionQuery } from "graphql";
import { plugin as runIntrospectionPlugin } from "@graphql-codegen/introspection";

// import { runIntrospection } from "./callIntroPlugin.js";

// type GraphQLInputType = {
//   name: string;
//   document: string;
//   uri: string;
//   variables: string;
//   headers: HeadersInit;
// };

export async function main(language: string): Promise<SerializedRenderResult> {
  // console.time("ExecutionTime");
  // const schema = JSON.parse(fs.readFileSync("/Users/2003j/dev/wfloat/gqlgen/schema/schema.json", "utf8"));

  // 1. https://github.com/prisma-labs/get-graphql-schema/blob/master/src/index.ts
  // const response = await fetch("http://localhost:4000/", {
  //   method: "POST",
  //   headers: { "Content-Type": "application/json" },
  //   body: JSON.stringify({ query: getIntrospectionQuery() }),
  // });
  // const schema = await response.json();

  // 2. Call introspection plugin function
  // const s = await runIntrospection();
  // const schema = JSON.parse(JSON.stringify(s));

  // for (let index = 0; index < 1000; index++) {
  const operationName = "AlbumsLinkMeta";
  const operation =
    "query AlbumsLinkMeta($options: PageQueryOptions) {albums(options: $options) {links {first {limit page}}meta {totalCount}}}";

  const schemaJson = fs.readFileSync("/home/mitch/dev/wfloat/packages/gqlgen/schema/schema.json", "utf8");
  // const schemaJson = fs.readFileSync("/Users/2003j/dev/wfloat/gqlgen/schema/schema.json", "utf8");

  const introspectionResultJson = JSON.parse(schemaJson as any);

  const schemaJson = fs.readFileSync("/home/mitch/dev/wfloat/packages/gqlgen/schema/schema.json", "utf8");
  const introspectionResultJson = JSON.parse(schemaJson as any);

  const source: GraphQLSourceData = {
    name: operationName,
    query: operation,
    schema: introspectionResultJson,
  };

  const inputData = new InputData();
  await inputData.addSource("graphql", source, () => new GraphQLInput());

  const languageName = language;
  // const lang = languageNamed(languageName, targetLanguages);
  const lang = new PythonTargetLanguage("Python", ["python", "py"], "py");
  const result = await quicktype({ lang, inputData });

  // for (const line of result.lines) {
  //   console.log(line);
  // }
  console.log(result.lines.join("\n"));
  return result;
}

// console.timeEnd("ExecutionTime");
// }

// const x = main("Python");

async function temp(): Promise<void> {
  const inputData = new InputData();
  const source = {
    name: "Player",
    schema: fs.readFileSync("src/GraphQLInputType.schema", "utf8"),
  };
  await inputData.addSource("schema", source, () => new JSONSchemaInput(undefined));

  const lang = new TypeScriptTargetLanguage();

  const { lines } = await quicktype({ lang, inputData });
  console.log(lines.join("\n"));
}
main("Python");
// temp();
