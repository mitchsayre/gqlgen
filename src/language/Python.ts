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
  JSONPythonRenderer,
} from "quicktype-core";
import { FixMeOptionsType } from "quicktype-core/dist/types";

export class PythonTargetLanguageGQL extends PythonTargetLanguage {
  constructor() {
    super("Python", ["python", "py"], "py");
  }

  protected makeRenderer(renderContext: RenderContext, untypedOptionValues: FixMeOptionsType): PythonRenderer {
    const options = getOptionValues(pythonOptions, untypedOptionValues);
    return new PythonRendererGQL(this, renderContext, options);
  }
}

class PythonRendererGQL extends JSONPythonRenderer {
  //   protected emitImports(): void {
  //     this.emitCommentLines(["TODO: This should show up at the top"]);
  //     this.emitMultiline(`import requests
  // import json`);
  //     super.emitImports();
  //   }
  //   protected emitClosingCode(): void {
  //     super.emitClosingCode();
  //     this.emitLine("# TODO: This should show up at the end");
  //     this.emitBlock(["def send_request(variables, url, headers):"], () => {
  //       this.emitMultiline(`payload = {
  //     "query": """query AlbumsLinkMeta($options: PageQueryOptions) {
  //         albums(options: $options) {
  //             links {
  //                 first {
  //                     limit
  //                     page
  //                 }
  //             }
  //             meta {
  //                 totalCount
  //             }
  //         }
  //     }""",
  //     "variables": variables
  // }
  //     response = requests.post(url, headers=headers, data=json.dumps(payload))
  //     result = response.json()
  //     return result`);
  //     });
  //     this.emitLine("\n");
  //     this.emitMultiline(`variables = {
  //     "options": {
  //         "paginate": {
  //             "limit": "10",
  //             "page": "2"
  //         },
  //         "search": {
  //             "q": "abc"
  //         },
  //         "slice": {
  //             "end": "xyz",
  //             "limit": "5"
  //         },
  //         "operators": [
  //             {
  //                 "field": "anime"
  //             }
  //         ]
  //     }
  // }
  // url = "http://localhost:4000/"
  // headers = {
  //     "Authorization": "<AUTH_TOKEN>",
  //     "Content-Type": "application/json"
  // }
  // result = send_request(variables, url, headers)
  // print(result)`);
  //   }
}
