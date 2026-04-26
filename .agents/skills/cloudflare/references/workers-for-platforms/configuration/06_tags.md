## Tags

Organize/search Workers (max 8/script):

```bash
# Set tags
curl -X PUT ".../tags" -d '["customer-123", "pro", "production"]'

# Filter by tag
curl ".../scripts?tags=production%3Ayes"

# Delete by tag
curl -X DELETE ".../scripts?tags=customer-123%3Ayes"
```

Common patterns: `customer-123`, `free|pro|enterprise`, `production|staging`

