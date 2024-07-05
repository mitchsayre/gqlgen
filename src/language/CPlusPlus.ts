import {
  quicktype,
  InputData,
  JSONSchemaInput,
  cSharpOptions,
  cPlusPlusOptions,
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
  CPlusPlusTargetLanguage,
  CPlusPlusRenderer,
} from "quicktype-core";

export class CPlusPlusTargetLanguageGQL extends CPlusPlusTargetLanguage {
  constructor() {
    super("CPlusPlus", ["cplusplus", "cpp"], "cpp");
  }

  protected makeRenderer(
    renderContext: RenderContext,
    untypedOptionValues: { [name: string]: any }
  ): CPlusPlusRenderer {
    return new CPlusPlusRendererGQL(this, renderContext, getOptionValues(cPlusPlusOptions, untypedOptionValues));
  }
}

class CPlusPlusRendererGQL extends CPlusPlusRenderer {
  protected emitUsageImportComment(): void {
    this.emitCommentLines(["TODO: This should show up at the top"]);
    this.emitMultiline(`#include <iostream>
#include <nlohmann/json.hpp>
#include <json/json.h>
#include <httplib.h>
using namespace std;
`);
  }

  protected emitModuleExports(): void {
    this.emitLine("# TODO: This should show up at the end");
    this.emitBlock(["nlohmann::json sendRequest() {"], true, () => {
      this.emitMultiline(`nlohmann::json sendRequest() {
  httplib::Client cli("localhost", 4000);

  nlohmann::json jsonBody = {
      {"query", "query VoiceModels($after: String) { VoiceModels(first: 50, after: $after) { edges { cursor node { checksumMD5ForAdded checksumMD5ForWeights checksumSHA256ForAdded checksumSHA256ForWeights filesizeForAdded filesizeForWeights hidden id name processed } } pageInfo { endCursor hasNextPage hasPreviousPage startCursor } } }"},
      {"operationName", "VoiceModels"},
      {"variables", {{"id", nullptr}}},
  };

  httplib::Headers headers = {
      {"Authorization", "<AUTHORIZATION_KEY>"},
      {"Content-Type", "application/json"}
  };

  auto res = cli.Post("/", headers, jsonBody.dump(), "application/json");

  return nlohmann::json::parse(res->body);`);
    });
    this.emitBlock(["int main() {"], true, () => {
      this.emitMultiline(`nlohmann::json result = sendRequest();
return 0;`);
    });
  }
}
