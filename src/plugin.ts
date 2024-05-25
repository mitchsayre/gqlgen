import { PluginFunction, PluginValidateFn, Types } from "@graphql-codegen/plugin-helpers";
import { GraphQLSchema } from "graphql";

/**
 * @description This is where we will define options the user can pass to our plugin. Like here: https://the-guild.dev/graphql/codegen/docs/custom-codegen/plugin-structure#add-plugin-configuration.
 */
export interface GqlGenConfig {}

export const plugin: PluginFunction<GqlGenConfig> = async (
  schema: GraphQLSchema,
  documents,
  config,
  info
): Promise<string> => {
  return `Plugin result output to out.txt...
  operation hashes: ${documents.map(doc => doc.hash).join(", ")}`;
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
