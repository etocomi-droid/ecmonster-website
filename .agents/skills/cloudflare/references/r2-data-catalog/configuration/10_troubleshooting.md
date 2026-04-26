## Troubleshooting

| Problem | Solution |
|---------|----------|
| 404 "catalog not found" | Run `wrangler r2 bucket catalog enable <bucket>` |
| 401 "unauthorized" | Check token has both Catalog + Storage permissions |
| 403 on data files | Token needs both permission groups |

See [gotchas.md](gotchas.md) for detailed troubleshooting.
