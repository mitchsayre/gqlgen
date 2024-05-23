# gqlgen

## Object oriented

```typescript
@Injectable({
  providedIn: "root",
})
export class FindUserGQL extends Apollo.Query<FindUserQuery, FindUserQueryVariables> {
  document = FindUserDocument;

  constructor(apollo: Apollo.Apollo) {
    super(apollo);
  }
}
```

## declarative

```typescript
import { graphql } from "../src/gql";

const allFilmsWithVariablesQueryDocument = graphql(`
  query allFilmsWithVariablesQuery($first: Int!) {
    allFilms(first: $first) {
      edges {
        node {
          ...FilmItem
        }
      }
    }
  }
`);

const { data } = useQuery(allFilmsWithVariablesQueryDocument, { variables: { first: 10 } });
```

## imperative

```typescript
import { findUserGQL } from "../src/generated";

findUserGQL(variables, uri, headers);
```
