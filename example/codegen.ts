import { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  schema: "./example/schema.graphql",
  documents: "./example/operations/**/*.graphql",
  generates: {
    "./example/generated/out.txt": {
      config: {
        language: "python", // This part here
      },
      plugins: ["./dist/plugin.js"],
    },
  },
};

export default config;
