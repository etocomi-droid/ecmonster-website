### not_found_handling Modes

| Mode | Behavior | Use Case |
|------|----------|----------|
| `"single-page-application"` | Serve `/index.html` for non-asset requests | React, Vue, Angular SPAs |
| `"404-page"` | Serve `/404.html` if exists, else 404 | Static sites with custom error page |
| `"none"` | Return 404 for missing assets | API-first or custom routing |

