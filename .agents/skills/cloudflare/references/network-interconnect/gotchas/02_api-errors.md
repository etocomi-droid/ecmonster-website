## API Errors

### 400 Bad Request: "slot_id already occupied"

**Cause:** Another interconnect already uses this slot  
**Solution:** Use `occupied=false` filter when listing slots:
```typescript
await client.networkInterconnects.slots.list({
  account_id: id,
  occupied: false,
  facility: 'EWR1',
});
```

### 400 Bad Request: "invalid facility code"

**Cause:** Typo or unsupported facility  
**Solution:** Check [locations PDF](https://developers.cloudflare.com/network-interconnect/static/cni-locations-2026-01.pdf) for valid codes

### 403 Forbidden: "Enterprise plan required"

**Cause:** Account not enterprise-level  
**Solution:** Contact account team to upgrade

### 422 Unprocessable: "validate_only request failed"

**Cause:** Dry-run validation found issues (wrong slot, invalid config)  
**Solution:** Review error message details, fix config before real creation

### Rate Limiting

**Limit:** 1200 requests/5min per token  
**Solution:** Implement exponential backoff, cache slot listings

