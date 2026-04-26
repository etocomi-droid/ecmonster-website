## Common Error Messages Reference

| Error Message | Likely Cause | Fix |
|---------------|--------------|-----|
| `401 Unauthorized` | Missing/invalid token | Check token has catalog+storage permissions |
| `403 Forbidden` | Token lacks storage permissions | Add R2 Storage Bucket Item permission |
| `404 Not Found` | Catalog not enabled or wrong URI | Run `wrangler r2 bucket catalog enable` |
| `409 Conflict` | Table/namespace already exists | Use try/except or load existing |
| `422 Unprocessable Entity` | Schema validation failed | Check type compatibility, required fields |
| `CommitFailedException` | Concurrent write conflict | Add retry logic with backoff |
| `NamespaceAlreadyExistsError` | Namespace exists | Use try/except or load existing |
| `NoSuchTableError` | Table doesn't exist | Check namespace+table name, create first |
| `TypeError: Cannot cast` | PyArrow type mismatch | Cast data to match Iceberg schema |

