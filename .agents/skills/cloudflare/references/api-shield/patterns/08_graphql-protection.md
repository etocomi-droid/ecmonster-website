## GraphQL Protection

```javascript
// Block oversized queries
(http.request.uri.path eq "/graphql" and
 cf.api_gateway.graphql_query_size gt 100000)
// Action: Block

// Block deep nested queries
(http.request.uri.path eq "/graphql" and
 cf.api_gateway.graphql_query_depth gt 10)
// Action: Block
```

