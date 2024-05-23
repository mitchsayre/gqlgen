// TODO
import {
  quicktype, 
  InputData, 
  JSONSchemaInput,
  cSharpOptions,
  tsFlowOptions,
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
  TypeScriptTargetLanguage,
  TypeScriptRenderer,
} from "quicktype-core";

export class TypeScriptTargetLanguageGQL extends TypeScriptTargetLanguage {
  private operationName: string;
  private operation: string;
  
  constructor(operationName: string, operation: string) {
    super();
    this.operationName = operationName;
    this.operation = operation;
  }

  protected makeRenderer(renderContext: RenderContext, untypedOptionValues: { [name: string]: any }): TypeScriptRenderer {
    return new TypeScriptRendererGQL(this, renderContext, getOptionValues(tsFlowOptions,untypedOptionValues));
  }
}

class TypeScriptRendererGQL extends TypeScriptRenderer {
  protected emitUsageImportComment(): void {
    this.emitCommentLines(["TODO: This should show up at the top"]);
    // this.emitMultiline();
    super.emitUsageImportComment();
  }

  protected emitModuleExports(): void {
    super.emitModuleExports();

    this.emitLine("# TODO: This should show up at the end");
    this.emitBlock(["const sendRequest() = async () => {"], "", () => {
      this.emitMultiline(`const response = await fetch("http://localhost:4000", {
method: "POST",
headers: {
Authorization: "<YOUR AUTH TOKEN HERE>",
"Content-Type": "application/json",
},
body: JSON.stringify({
query: "query VoiceModels($after: String) { VoiceModels(first: 50, after: $after) { edges { cursor node { checksumMD5ForAdded checksumMD5ForWeights checksumSHA256ForAdded checksumSHA256ForWeights filesizeForAdded filesizeForWeights hidden id name processed } } pageInfo { endCursor hasNextPage hasPreviousPage startCursor } } }",
operationName: "VoiceModels",
variables: { id: null },
}),
});

const result = await response.json();
return result;
}`);
    });
  }
}
