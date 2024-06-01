// import { CodegenConfig, generate } from "@graphql-codegen/cli";
// import * as path from 'path';
// import glob from 'glob';

// const documentsPath = "./example/operations/**/*.graphql";
// const outputPath = "./example/generated";
// const indexFilePath = "./src/language/TypeScript.ts"; // Path to TypeScript.ts

// const config: CodegenConfig = {
//   schema: "./example/schema.graphql",
//   documents: documentsPath,
//   generates: {},
// };

// const files = glob.sync(documentsPath).concat([indexFilePath]); // get each file

// files.forEach (file=>{
//   let fileName, outputFile;
//   if(file === indexFilePath){
//     fileName = path.basename("index", '.ts');
//     outputFile = path.join(outputPath, `${fileName}.ts`);

//   } // index file (TypeScript.ts)
//   else {
//     fileName = path.basename(file, '.graphql');
//     outputFile = path.join(outputPath, `${fileName}.ts`);
//   }

//   config.generates[outputFile] = {
//     config: {
//       language: "Typescript",
//       fName: fileName,
//     },
//     plugins: ["./dist/plugin.js"],
//   };
// });

// generate(config);

// export default config;

import { CodegenConfig } from "@graphql-codegen/cli";

const config: CodegenConfig = {
  schema: "./example/schema.graphql",
  documents: "./example/operations/**/*.graphql",
  generates: {
    // "./example/generated/out.txt": {
    //   config: {
    //     language: "Python", // This part here
    //   },
    //   plugins: ["./dist/plugin.js"],
    // },
    "./example/generated/": {
      preset: "near-operation-file",
      presetConfig: {
        extension: ".ex",
        baseTypesPath: "index.test",
      },
      plugins: ["./dist/plugin.js"],
    },
  },
};

export default config;
