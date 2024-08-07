import { TargetLanguage } from "quicktype-core";
import { PythonTargetLanguageGQL } from "./Python.js";
import { TypeScriptTargetLanguageGQL } from "./TypeScript.js";
import { ElixirTargetLanguageGQL } from "./Elixir.js";
import { CPlusPlusTargetLanguageGQL } from "./CPlusPlus.js";

export * from "./CPlusPlus.js";
export * from "./Elixir.js";
export * from "./Python.js";
export * from "./TypeScript.js";

export const targetLanguages: TargetLanguage[] = [
  new PythonTargetLanguageGQL(),
  new TypeScriptTargetLanguageGQL(),
  new ElixirTargetLanguageGQL(),
  new CPlusPlusTargetLanguageGQL(),
];
