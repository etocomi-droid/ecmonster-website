## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Tail consumer not found" | Not deployed | Deploy tail Worker first |
| "No tail handler" | Missing `tail()` | Add to default export |
| "waitUntil is not a function" | Missing `ctx` | Add `ctx` parameter |
| Timeout | Blocking await | Use `ctx.waitUntil()` |

