import {
  quicktype,
  InputData,
  JSONSchemaInput,
  cSharpOptions,
  pythonOptions,
  CSharpRenderer,
  RenderContext,
  getOptionValues,
  Sourcelike,
  ClassType,
  Type,
  TypeAttributeKind,
  JSONSchema,
  Ref,
  JSONSchemaType,
  JSONSchemaAttributes,
  ClassProperty,
  Name,
  PythonTargetLanguage,
  PythonRenderer,
} from "quicktype-core";

export class PythonTargetLanguageGQL extends PythonTargetLanguage {
  constructor() {
    super("Python", ["python", "py"], "py");
  }

  protected makeRenderer(renderContext: RenderContext, untypedOptionValues: { [name: string]: any }): PythonRenderer {
    return new PythonRendererGQL(this, renderContext, getOptionValues(pythonOptions, untypedOptionValues));
  }
}

class PythonRendererGQL extends PythonRenderer {
  protected emitImports(): void {
    this.emitCommentLines(["TODO: This should show up at the top"]);
    this.emitMultiline(`import requests
import json`);
    super.emitImports();
  }

  protected emitClosingCode(): void {
    super.emitClosingCode();

    this.emitLine("# TODO: This should show up at the end");
    this.emitBlock(["def send_request():"], () => {
      this.emitMultiline(`url = "http://localhost:4000"
        headers = {
            "Authorization": "<DONT_COMMIT_AUTH_TOKEN_TO_GITHUB>",
            "Content-Type": "application/json"
        }
        payload = {
            "query": """query VoiceModels($after: String) { VoiceModels(first: 2, after: $after) { edges { cursor node { checksumMD5ForAdded checksumMD5ForWeights checksumSHA256ForAdded checksumSHA256ForWeights filesizeForAdded filesizeForWeights hidden id name processed } } pageInfo { endCursor hasNextPage hasPreviousPage startCursor } } }""",
            "operationName": "VoiceModels",
            "variables": {"id": None}
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

        result = response.json()
        return result`);
    });
  }
}
