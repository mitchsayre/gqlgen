import { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  schema: "./example/schema.graphql",
  documents: "./example/operations/**/*.graphql",
  generates: {
    "./example/generated/out.txt": {
      plugins: ["./dist/plugin.js"],
    },
  },
};

export default config;
