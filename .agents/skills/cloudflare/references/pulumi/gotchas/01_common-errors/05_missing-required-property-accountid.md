### "Missing required property 'accountId'"

**Problem:** `Error: Missing required property 'accountId'`  
**Cause:** Account ID not provided in resource configuration  
**Solution:** Add to stack config

```yaml
# Pulumi.<stack>.yaml
config:
  cloudflare:accountId: "abc123..."
```

