import { PluginFunction, PluginValidateFn, Types, isComplexPluginOutput } from "@graphql-codegen/plugin-helpers";
import { GraphQLSchema } from "graphql";

/**
 * @description This is where we will define options the user can pass to our plugin. Like here: https://the-guild.dev/graphql/codegen/docs/custom-codegen/plugin-structure#add-plugin-configuration.
 */

export interface GqlGenConfig {
  language: string; // Add the language property to the config interface
}

export const plugin: PluginFunction<GqlGenConfig> = async (
  schema: GraphQLSchema,
  documents,
  config,
  info
): Promise<string> => {
  // info!.allPlugins![0].add = [];
  // console.log(config);
  // console.log(documents.length, "length");
  console.log(`
  
  
  
  aaaaaaaa
  
  
  
  `);
  // console.log(info!.allPlugins![0].add);
  // console.log(`

  // `);
  return `Plugin result output to out.txt...
  operation hashes: ${documents.map(doc => doc.hash).join(", ")}
  language: ${config.language}`;
};

export const validate: PluginValidateFn<any> = async (
  schema: GraphQLSchema,
  documents: Types.DocumentFile[],
  config: GqlGenConfig,
  outputFile: string,
  allPlugins: Types.ConfiguredPlugin[]
) => {
  // We can validate the conditions that our plugin needs here and throw errors if necessary.
};
