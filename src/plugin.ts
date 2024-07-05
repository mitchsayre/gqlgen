import { PluginFunction, PluginValidateFn, Types, isComplexPluginOutput } from "@graphql-codegen/plugin-helpers";
import { GraphQLSchema, OperationDefinitionNode } from "graphql";
import { GraphQLInput, GraphQLSourceData } from "quicktype-graphql-input";
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
} from "quicktype-core";
import { targetLanguages } from "./language";

/**
 * @description This is where we will define options the user can pass to our plugin. Like here: https://the-guild.dev/graphql/codegen/docs/custom-codegen/plugin-structure#add-plugin-configuration.
 */

export interface GqlgenConfig {
  language: string; // Add the language property to the config interface
  introspectionResultJson: any;
  namespace: string;
}

export const plugin: PluginFunction<GqlgenConfig> = async (
  schema: GraphQLSchema,
  documents,
  config,
  info
): Promise<string> => {
  const document = documents[0];
  const operationDefinition = document.document?.definitions.find(
    def => def.kind === "OperationDefinition"
  ) as OperationDefinitionNode;
  const operationName = operationDefinition.name?.value!;

  const source: GraphQLSourceData = {
    name: operationName,
    query: document.rawSDL!,
    schema: config.introspectionResultJson,
  };
  const inputData = new InputData();
  await inputData.addSource("graphql", source, () => new GraphQLInput());

  const lang = languageNamed(config.language, targetLanguages);
  const result = await quicktype({
    lang,
    inputData,
    rendererOptions: {
      namespace: config.namespace, // "MyNamespace.Foobar.UpdateComment",
      // "just-types": false,
      // "just-types": "false",
      // "python-version": "3.7",
      "prefer-types": true,
    },
  });

  return `${result.lines.join("\n")}`;
};

export const validate: PluginValidateFn<any> = async (
  schema: GraphQLSchema,
  documents: Types.DocumentFile[],
  config: GqlgenConfig,
  outputFile: string,
  allPlugins: Types.ConfiguredPlugin[]
) => {
  // We can validate the conditions that our plugin needs here and throw errors if necessary.
};
