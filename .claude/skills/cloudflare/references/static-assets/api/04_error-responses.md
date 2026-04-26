## Error Responses

| Status | Condition | Behavior |
|--------|-----------|----------|
| `404` | Asset not found | Body depends on `not_found_handling` config |
| `405` | Non-GET/HEAD method | `{ "error": "Method not allowed" }` |
| `416` | Invalid Range header | Range not satisfiable |

### 404 Handling

Depends on configuration (see configuration.md:45-52):

```typescript
// not_found_handling: "single-page-application"
// Returns /index.html with 200 status

// not_found_handling: "404-page"
// Returns /404.html if exists, else 404 response

// not_found_handling: "none"
// Returns 404 response
```

