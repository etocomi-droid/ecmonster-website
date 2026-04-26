## Schema Introspection

```graphql
# List zone-scoped datasets
{ __type(name: "zone") { fields { name description } } }

# List account-scoped datasets
{ __type(name: "account") { fields { name description } } }

# Discover dimensions for a dataset
{ __type(name: "ZoneHttpRequestsAdaptiveGroupsDimensions") {
  fields { name type { name kind } }
} }

# Discover filter operators for a dataset
{ __type(name: "ZoneHttpRequestsAdaptiveGroupsFilter_InputObject") {
  inputFields { name type { name kind } }
} }
```

