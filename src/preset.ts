import { promises as fs, existsSync } from "fs";
import path from "path";
import { buildASTSchema, DocumentNode, GraphQLSchema, Kind } from "graphql";
import { Types } from "@graphql-codegen/plugin-helpers";
import { FragmentImport, ImportSource } from "@graphql-codegen/visitor-plugin-common";
import type { Source } from "@graphql-tools/utils";
import { plugin as runIntrospectionPlugin } from "@graphql-codegen/introspection";
import * as entrypointPlugin from "./entrypointPlugin";

export type FragmentImportFromFn = (
  source: ImportSource<FragmentImport>,
  sourceFilePath: string
) => ImportSource<FragmentImport>;

export type GqlgenPresetConfig = {
  language: keyof typeof languages;
  extension?: string;
  preserveFiles?: string[];
};

const languages = {
  Python: {
    extension: "py",
    filenameCaseStyle: "snake",
  },
  TypeScript: {
    extension: "ts",
    filenameCaseStyle: "pascal",
  },
  Elixir: {
    extension: "ex",
    filenameCaseStyle: "snake",
  },
  CPlusPlus: {
    extension: "cpp",
    filenameCaseStyle: "pascal",
  },
};

async function emptyDirectory(dirPath: string, preserveFiles?: string[]): Promise<void> {
  if (!existsSync(dirPath)) {
    return;
  }

  const files = await fs.readdir(dirPath);
  for (const file of files) {
    if (preserveFiles) {
      if (!preserveFiles.includes(file)) {
        const fullPath = path.join(dirPath, file);
        await fs.rm(fullPath, { recursive: true });
      }
    }
  }
}

export const preset: Types.OutputPreset<GqlgenPresetConfig> = {
  buildGeneratesSection: async options => {
    await emptyDirectory(options.baseOutputDir, options.presetConfig.preserveFiles);

    const schemaObject: GraphQLSchema = options.schemaAst
      ? options.schemaAst
      : buildASTSchema(options.schema, options.config as any);

    const sources = options.documents.map(documentFile => {
      let filename = path.basename(documentFile.location!, path.extname(documentFile.location!));
      const language = options.presetConfig.language as keyof typeof languages;
      const languageInfo = languages[language];
      if (languageInfo.filenameCaseStyle === "snake") {
        filename = filename
          .split(/\.?(?=[A-Z])/)
          .join("_")
          .toLowerCase();
      }
      filename = path.join(
        options.baseOutputDir,
        `${filename}.${options.presetConfig.extension ?? languageInfo.extension}`
      );
      return {
        filename,
        documents: [documentFile],
      };
    });

    const filePathsMap = new Map<
      string,
      {
        documents: Array<Source>;
      }
    >();

    for (const source of sources) {
      let record = filePathsMap.get(source.filename);
      if (record === undefined) {
        record = {
          documents: [],
        };
        filePathsMap.set(source.filename, record);
      }
      record.documents.push(...source.documents);
    }

    const artifacts: Array<Types.GenerateOptions> = [];

    for (const [filename, record] of filePathsMap.entries()) {
      const plugins = [...options.plugins];

      const introspectionResult = await runIntrospectionPlugin(schemaObject, options.documents, options.config);
      const introspectionResultJson = { data: JSON.parse(introspectionResult as any) };

      const config = {
        ...options.config,
        language: options.presetConfig.language,
        introspectionResultJson: introspectionResultJson,
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
      });
    }

    const entrypointPlugins: Array<Types.ConfiguredPlugin> = [
      { [`entrypointPlugin`]: { content: `/* eslint-disable */` } },
    ];
    const entrypointPluginMap = { [`entrypointPlugin`]: entrypointPlugin } as any;
    const entrypointArtifact: Types.GenerateOptions = {
      ...options,
      filename: path.join(options.baseOutputDir, "__init__.py"),
      documents: options.documents,
      plugins: entrypointPlugins,
      pluginMap: entrypointPluginMap,
      config: {},
      schema: options.schema,
      schemaAst: schemaObject,
    };
    artifacts.push(entrypointArtifact);

    return artifacts;
  },
};

export default preset;
