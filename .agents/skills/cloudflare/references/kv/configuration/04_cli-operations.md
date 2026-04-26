## CLI Operations

```bash
# Put
wrangler kv key put --binding=MY_KV "key" "value"
wrangler kv key put --binding=MY_KV "key" --path=./file.json --ttl=3600

# Get
wrangler kv key get --binding=MY_KV "key"

# Delete
wrangler kv key delete --binding=MY_KV "key"

# List
wrangler kv key list --binding=MY_KV --prefix="user:"

# Bulk operations (max 10,000 keys per file)
wrangler kv bulk put data.json --binding=MY_KV
wrangler kv bulk get keys.json --binding=MY_KV
wrangler kv bulk delete keys.json --binding=MY_KV --force
```

