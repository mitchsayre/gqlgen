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
} from "quicktype-core";
import { GraphQLInput, GraphQLSourceData } from "quicktype-graphql-input";
import { PythonTargetLanguageGQL } from "./language/Python.js";
import { targetLanguages } from "./language/index.js";
// import { makeQuicktypeOptions, CLIOptions } from "quicktype";

// type GraphQLInputType = {
//   name: string;
//   document: string;
//   uri: string;
//   variables: string;
//   headers: HeadersInit;
// };

export async function main(): Promise<void> {
  // console.time("ExecutionTime");
  const schema = JSON.parse(fs.readFileSync("/Users/2003j/dev/wfloat/gqlgen/schema/schema.json", "utf8"));

  // for (let index = 0; index < 1000; index++) {

  const operationName = "AIHubVoiceModels";
  const operation =
    "query AIHubVoiceModels($after: String) { AIHubVoiceModels(first: 100, minDownloadCount: 75, after: $after) { pageInfo { endCursor hasNextPage hasPreviousPage startCursor } edges { node { downloadCount filename name checksumMD5ForWeights inferredProfile { accent confidence fictional gender id modelTrainedOnEnglishProbability name nativeLanguage relevantTags voiceModelId } backupUrls(first: 20) { edges { node { id url voiceModelId } } } } } } }";

  const source: GraphQLSourceData = {
    name: operationName,
    query: operation,
    schema: schema,
  };

  const inputData = new InputData();
  await inputData.addSource("graphql", source, () => new GraphQLInput());

  const languageName = "TypeScript";
  const lang = languageNamed(languageName, targetLanguages);
  const result = await quicktype({ lang, inputData });

  for (const line of result.lines) {
    console.log(line);
  }
}

// console.timeEnd("ExecutionTime");
// }

// main();

async function temp(): Promise<void> {
  const inputData = new InputData();
  const source = {
    name: "Player",
    schema: fs.readFileSync("src/GraphQLInputType.schema", "utf8"),
  };
  await inputData.addSource("schema", source, () => new JSONSchemaInput(undefined));

  const lang = new TypeScriptTargetLanguage();

  const { lines } = await quicktype({ lang, inputData });

  for (const line of lines) {
    console.log(line);
  }
}
temp();
