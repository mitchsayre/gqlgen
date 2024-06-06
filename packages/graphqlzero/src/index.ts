import { ApolloServer } from "@apollo/server";
import { typeDefs } from "./type-defs";
import { resolvers } from "./resolvers";
import { startStandaloneServer } from "@apollo/server/standalone";

const port = 4000;

const server = new ApolloServer({
  typeDefs,
  resolvers,
  introspection: true,
});

async function startServer() {
  const { url } = await startStandaloneServer(server, {
    listen: { port },
    context: async ({ req, res }): Promise<any> => {},
  });

  console.log(`🚀 Server ready at: ${url}`);
}

startServer();
