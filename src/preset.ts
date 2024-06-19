import path from "path";
import { buildASTSchema, DocumentNode, FragmentDefinitionNode, GraphQLSchema, Kind } from "graphql";
// import addPlugin from "@graphql-codegen/add";
import { CodegenPlugin, Types } from "@graphql-codegen/plugin-helpers";
import {
  FragmentImport,
  getConfigValue,
  ImportDeclaration,
  ImportSource,
  LoadedFragment,
} from "@graphql-codegen/visitor-plugin-common";
import type { Source } from "@graphql-tools/utils";
import { DocumentImportResolverOptions, resolveDocumentImports } from "./resolve-document-imports.js";
import { appendFileNameToFilePath, defineFilepathSubfolder } from "./utils.js";
import { plugin as runIntrospectionPlugin } from "@graphql-codegen/introspection";

export { resolveDocumentImports, DocumentImportResolverOptions };

export type FragmentImportFromFn = (
  source: ImportSource<FragmentImport>,
  sourceFilePath: string
) => ImportSource<FragmentImport>;

export type GqlGenPresetConfig = {
  /**
   * @description Optional, sets the extension for the generated files. Use this to override the extension if you are using plugins that requires a different type of extensions (such as `typescript-react-apollo`)
   * @default .generated.ts
   *
   * @exampleMarkdown
   * ```ts filename="codegen.ts" {11}
   *  import type { CodegenConfig } from '@graphql-codegen/cli';
   *
   *  const config: CodegenConfig = {
   *    // ...
   *    generates: {
   *      'path/to/file.ts': {
   *        preset: 'near-operation-file',
   *        plugins: ['typescript-operations', 'typescript-react-apollo'],
   *        presetConfig: {
   *          baseTypesPath: 'types.ts',
   *          extension: '.generated.tsx',
   *        },
   *      },
   *    },
   *  };
   *  export default config;
   * ```
   */
  extension?: string;
};

// export type FragmentNameToFile = {
//   [fragmentName: string]: {
//     location: string;
//     importsNames: string[];
//     onType: string;
//     node: FragmentDefinitionNode;
//   };
// };

export const preset: Types.OutputPreset<GqlGenPresetConfig> = {
  buildGeneratesSection: async options => {
    const startTime = performance.now();

    const schemaObject: GraphQLSchema = options.schemaAst
      ? options.schemaAst
      : buildASTSchema(options.schema, options.config as any);

    // const baseDir = options.presetConfig.cwd || process.cwd();
    // const fileName = options.presetConfig.fileName || "";
    const extension = options.presetConfig.extension;

    const pluginMap: { [name: string]: CodegenPlugin } = {
      ...options.pluginMap,
      // add: addPlugin, TODO: add entrypoint and utils plugins
    };

    const baseDir = process.cwd();

    const sources = resolveDocumentImports(
      options,
      schemaObject,
      {
        baseDir,
        generateFilePath(location: string) {
          const filename = path.basename(location, path.extname(location));
          return path.join(options.baseOutputDir, `${filename}.py`);
        },
        schemaTypesSource: {
          path: path.join(options.baseOutputDir),
          namespace: "NamespaceHere",
        },
        typesImport: options.config.useTypeImports ?? false,
      },
      getConfigValue(options.config.dedupeFragments, false)
    );

    // console.log(sources, "sources here!\n\n\n\n");

    const filePathsMap = new Map<
      string,
      {
        importStatements: Set<string>;
        documents: Array<Source>;
        externalFragments: Array<
          LoadedFragment<{
            level: number;
          }>
        >;
        fragmentImports: Array<ImportDeclaration<FragmentImport>>;
      }
    >();

    for (const source of sources) {
      // console.log(source, "source here!");
      let record = filePathsMap.get(source.filename);
      if (record === undefined) {
        record = {
          importStatements: new Set(),
          documents: [],
          externalFragments: [],
          fragmentImports: [],
        };
        filePathsMap.set(source.filename, record);
      }

      // for (const importStatement of source.importStatements) {
      //   record.importStatements.add(importStatement);
      // }
      record.documents.push(...source.documents);
      record.externalFragments.push(...source.externalFragments);
      record.fragmentImports.push(...source.fragmentImports);
    }

    const artifacts: Array<Types.GenerateOptions> = [];

    for (const [filename, record] of filePathsMap.entries()) {
      let fragmentImportsArr = record.fragmentImports;

      if (false) {
        fragmentImportsArr = record.fragmentImports.map<ImportDeclaration<FragmentImport>>(t => {
          const newImportSource: ImportSource<FragmentImport> =
            typeof importAllFragmentsFrom === "string"
              ? { ...t.importSource, path: importAllFragmentsFrom }
              : importAllFragmentsFrom(t.importSource, filename);

          return {
            ...t,
            importSource: newImportSource || t.importSource,
          };
        });
      }

      // Merge multiple fragment imports from the same file
      const fragmentImportsByImportSource: Record<string, ImportDeclaration<FragmentImport>> = {};
      fragmentImportsArr.forEach(fi => {
        if (!fragmentImportsByImportSource[fi.importSource.path]) {
          fragmentImportsByImportSource[fi.importSource.path] = fi;
        } else {
          const mergedIdentifiersByName = {};
          fragmentImportsByImportSource[fi.importSource.path].importSource.identifiers.forEach(identifier => {
            mergedIdentifiersByName[identifier.name] = identifier;
          });
          fi.importSource.identifiers.forEach(identifier => {
            mergedIdentifiersByName[identifier.name] = identifier;
          });
          fragmentImportsByImportSource[fi.importSource.path].importSource.identifiers =
            Object.values(mergedIdentifiersByName);
        }
      });
      fragmentImportsArr = Object.values(fragmentImportsByImportSource);

      // top level
      // entry point
      // utils

      const plugins = [
        // // TODO/NOTE I made globalNamespace include schema types - is that correct?
        // ...(options.config.globalNamespace
        //   ? []
        //   : Array.from(record.importStatements).map(importStatement => ({
        //       add: { content: importStatement },
        //     }))),
        ...options.plugins,
      ];

      const introspectionResult = await runIntrospectionPlugin(schemaObject, options.documents, options.config);
      const introspectionResultJson = { data: JSON.parse(introspectionResult as any) };

      const config = {
        ...options.config,
        introspectionResultJson: introspectionResultJson,
        // This is set here in order to make sure the fragment spreads sub types
        // are exported from operations file
        // exportFragmentSpreadSubTypes: true,
        // namespacedImportName: "NamespaceHereAAA",
        // externalFragments: record.externalFragments,
        // fragmentImports: fragmentImportsArr,
      };

      const document: DocumentNode = { kind: Kind.DOCUMENT, definitions: [] };
      const combinedSource: Source = {
        rawSDL: "",
        document,
        location: record.documents[0].location,
      };

      for (const source of record.documents) {
        if (source.rawSDL) {
          combinedSource.rawSDL += source.rawSDL;
        }

        if (combinedSource.document && source.document) {
          (combinedSource.document.definitions as any).push(...source.document.definitions);
        }
      }

      artifacts.push({
        ...options,
        filename,
        documents: [combinedSource],
        plugins,
        config,
        schema: options.schema,
        schemaAst: schemaObject,
        // skipDocumentsValidation:
        //   typeof options.config.skipDocumentsValidation === "undefined"
        //     ? { skipDuplicateValidation: true }
        //     : options.config.skipDocumentsValidation,
      });
    }

    // console.log(introspectionResult, "introspectionResult");
    // console.log("artifactshere", artifacts);

    artifacts.forEach((artifact, index) => {
      // console.log(`artifact ${index} length: ${artifact.filename}`);
      Object.entries(artifact).forEach(([key, value]) => {
        // console.log(`${key}: ${value}`);
      });
      // console.log(`--------------------

      // `);
    });

    // console.log(
    //   artifacts,
    //   `

    // `
    // );
    const endTime = performance.now();
    const duration = endTime - startTime;
    console.log(`The function took ${duration} milliseconds.`);
    return artifacts;
  },
};

export default preset;
