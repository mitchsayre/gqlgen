import { ApolloServer } from "@apollo/server";
import { ApolloServerPluginLandingPageGraphQLPlayground } from "@apollo/server-plugin-landing-page-graphql-playground";
import { typeDefs } from "./type-defs";
import { resolvers } from "./resolvers";
import { startStandaloneServer } from "@apollo/server/standalone";
import express from "express";
import { expressMiddleware } from "@apollo/server/express4";
import bodyParser from "body-parser";

const app = express();
const port = 4000;

const server = new ApolloServer({
  typeDefs,
  resolvers,
  introspection: true,
  plugins: [
    ApolloServerPluginLandingPageGraphQLPlayground({
      settings: {
        "editor.theme": "light",
      },
    }),
  ],
});

async function startServer() {
  await server.start();
  app.use("/graphql", bodyParser.json(), expressMiddleware(server));
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}/graphql`);
  });
}

startServer();

// const startServer = async () => {
//   await server.start();

//   const app = express();

//   app.use(
//     "/graphql",
//     bodyParser.json(),
//     expressMiddleware(server, {
//       context: async ({ req }) => ({ req }),
//     })
//   );

//   const port = 4000;

//   app.listen(port, () => {
//     console.log(`Server is running on http://localhost:${port}/graphql`);
//   });
// };

// startServer();
