import { plugin as introspectionPlugin, IntrospectionPluginConfig } from "./introspectionPlugin";
import { buildSchema, GraphQLSchema } from "graphql";
import * as fs from "fs";
// Define your GraphQL schema
const schemaSDL: string = fs.readFileSync("../example/schema.graphql", "utf-8");

const schema: GraphQLSchema = buildSchema(schemaSDL);

// Define the plugin configuration
const pluginConfig: IntrospectionPluginConfig = {
  minify: true,
  descriptions: true,
  specifiedByUrl: true,
  directiveIsRepeatable: true,
  schemaDescription: true,
};

// Call the plugin function
export async function runIntrospection() {
  const introspectionResult = await introspectionPlugin(schema, [], pluginConfig);
  // Use introspectionResult as needed
  return introspectionResult;
}
