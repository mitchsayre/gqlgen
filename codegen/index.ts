import { CodegenConfig } from '@graphql-codegen/cli';
 
const config: CodegenConfig = {
  schema: '',
  generates: {
    './src/output.ts': {
      plugins: ['./src/watch.ts'],
    }
  }
};
export default config;
 