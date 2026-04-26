## Catalog URI Issues

### 404 Not Found

**Error:** `"404 Catalog not found"`  
**Cause:** Catalog not enabled or wrong URI.  
**Solution:** Run `wrangler r2 bucket catalog enable <bucket>`. URI must be HTTPS with `/iceberg/` and case-sensitive bucket name.

### Wrong Warehouse

**Error:** Cannot create/load tables.  
**Cause:** Warehouse ≠ bucket name.  
**Solution:** Set `warehouse="bucket-name"` to match bucket exactly.

