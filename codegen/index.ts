import { CodegenConfig } from '@graphql-codegen/cli';

const config: CodegenConfig = {
  schema: './codegen/schema.gql',
  documents: './operations/*.graphql',
  generates: {
    './src/output.ts': {
      plugins: ['./src/watch.ts'],
    },
  },
};

export default config;
