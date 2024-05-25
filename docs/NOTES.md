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

## Declarative

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

## Imperative

```typescript
import { findUserGQL } from "../src/generated";

findUserGQL(variables, uri, headers);
```
