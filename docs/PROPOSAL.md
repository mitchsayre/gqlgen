# Proposal

## Introduction:

The project will generate type-safe GraphQL client-side code from defined queries and mutations in many programming languages, all from the same codebase. The generated code will be fully type-safe for both an operation’s response as well as its input variables. It will work seamlessly as a plugin for graphql-code-generator.

## Overview:

The project will generate GraphQL clients for programming languages that currently may not have a type-safe option in the community. Additionally, if an organization uses multiple programming languages, the proposed project will reduce complexity in the organization's build process as they develop locally and introduce a more favorable separation of concerns. That is, instead of each service being responsible for generating GraphQL client code itself, the proposed project will generate clients to a specified location in the service’s code. All clients will be regenerated whenever the API schema changes, so they will be fresh when services are recompiled and started by the programmer. This simplifies the code within an organization and prevents race conditions that may occur if a developer restarts the program before one of the services detected an API schema change or finished generating a fresh client for itself.

The project will be written in TypeScript and distributed as a Node.js package that is usable on its own or as a plugin for graphql-code-generator. The project will heavily depend on QuickType, which “generates strongly-typed models and serializers from JSON, JSON Schema, TypeScript, and GraphQL queries, making it a breeze to work with JSON type-safely in many programming languages.” [[1]](https://github.com/glideapps/quicktype)

QuickType already supports generating types for an operation response but needs support for generating types for an operation’s input arguments. I will add this feature to QuickType. A pull request was started for this feature [[2]](https://github.com/glideapps/quicktype/issues/1211)[[3]](https://github.com/FishandRichardsonPC/GraphQL.Typed.Client/issues/1), and I will salvage some of the code from it. I am confident I can complete this feature since I recently added Elixir support to QuickType [[4]](https://github.com/glideapps/quicktype/pull/2553) and understand its codebase. From there, the project will generate code that executes each operation alongside the types/structs produced by QuickType for the operation’s input arguments and response data. Included alongside the generated operations will be a single top-level file that includes generic code to execute a network request for the operations. The top-level file will also export each operation if the target language requires this, allowing the generated code to be used as a package.

## Motivation:

Of the 52 GraphQL clients listed on graphql.org [[5]](https://graphql.org/community/tools-and-libraries/?tags=client), I read their documentation and determined that only 10 support generating code from operations out of the box. The count increases to 15 when including clients that have their own graphql-code-generator plugins or can be made to work with plugins. Another 8 clients support a different codegen approach that generates types via introspection. The programmer then constructs operations as code from these generated types, and the operations are stringified at runtime [[6]](https://github.com/mitchsayre/gqlgen/blob/main/docs/clients.csv). This approach is advantageous for specific use cases, but for most applications, I find that defining operations using the .graphql DSL directly to generate operation code for the target programming language yields better results.

A more detailed analysis of the clients listed on graphql.org, which support codegen from operations, shows that 6 are in Typescript, 2 are in Kotlin, 1 is in Swift, 1 is in Python, 1 is in Go, 1 is in Dart, 1 is in C#/.NET, 1 is in Haskell, 0 are in Elixir, 0 are in Scala, 0 are in Objective-C, 0 are in C++, and 0 are in Ruby. Note that these results do not perfectly represent all the options out there. For example, none of the Rust clients on the list support codegen from operations, but I found a popular Rust package that supports it [[7]](https://github.com/graphql-rust/graphql-client).

While some programming languages have at least one client available, several popular languages still have no options. Organizations that already use GraphQL might find themselves forced to forgo a language that would otherwise be ideal for their specific use case due to a lack of support. Similarly, organizations considering the adoption of GraphQL might decide against it if they have existing programs written in a language that is not supported.

Additionally, the GraphQL clients that do support codegen from operations all have unique setup requirements and configurations. They also have different approaches for working with their generated code that go beyond the basic features, constraints, and stylistic choices of their target language. This makes sense, as all of the clients were written and maintained in relative isolation from one another. However, these differences nonetheless pose a challenge for developers working in codebases that use multiple programming languages.

## Benefit to the community:

The proposed project introduces a significant advancement in developing multi-language applications by centralizing the generation of type-safe GraphQL clients. Developers will be empowered to select programming languages for their use case without being limited by their API. They will have confidence that their program respects the latest API changes with error detection and resolution during development rather than in later unit testing or quality assurance phases. As a result, teams can allocate more resources toward enhancing application performance and user experience, ultimately boosting productivity and software reliability.

- [1] https://github.com/glideapps/quicktype
- [2] https://github.com/glideapps/quicktype/issues/1211
- [3] https://github.com/FishandRichardsonPC/GraphQL.Typed.Client/issues/1
- [4] https://github.com/glideapps/quicktype/pull/2553
- [5] https://graphql.org/community/tools-and-libraries/?tags=client
- [6] https://github.com/mitchsayre/gqlgen/blob/main/docs/clients.csv
- [7] https://github.com/graphql-rust/graphql-client
