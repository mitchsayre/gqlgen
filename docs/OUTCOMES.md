# Outcomes

The project will generate working, fully type-safe GraphQL clients in Elixir (using Dialyxir [[8]](https://github.com/jeremyjh/dialyxir)), C++, Python, and TypeScript, as well as some other languages the GraphQL foundation believes should be supported. The project will be designed in a way that enables supporting more languages in the future. The project will have extensive unit tests that run in GitHub actions. The unit tests for the project will be complicated as they will need to target many languages, however, QuickType has this approach built into its CI already [[9]](https://github.com/glideapps/quicktype/blob/master/.github/workflows/test-pr.yaml), and I will model this approach. Using the generated client code should be as similar as possible across target languages while still conforming to language-specific conventions and styles.

For testing, A lightweight GraphQL server written in TypeScript will run locally, and each language will be tested against it. Testing does not need to focus on the validity of the generated types/structs since QuickType already heavily tests this. Rather, testing should focus on the success of the network requests issued for the operation and converting the server responses to the specific language.

QuickType supports fragments, so the project will as well. Subscriptions will not be supported in the initial version of the project, but they can be added in the future. Client-side caching will not be supported, but I believe this is acceptable because many clients for single-page and mobile applications already work well with graphql-code-generator.

Finally, documentation for each target language will be supplied with clear and straightforward examples of how to use the generated code to run operations.

- [8] https://github.com/jeremyjh/dialyxir
- [9] https://github.com/glideapps/quicktype/blob/master/.github/workflows/test-pr.yaml
