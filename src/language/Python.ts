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
    uery AlbumsLinkMeta($options: PageQueryOptions) {
        albums(options: $options) {
            links {
                first {
                    limit
                    page
                }
            }
            meta {
                totalCount
            }
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

result = response.json()
return result`);
    });
  }
}
