## Permission Errors

### 401 Unauthorized

**Error:** `"401 Unauthorized"`  
**Cause:** Token missing R2 Data Catalog permissions.  
**Solution:** Use "Admin Read & Write" token (includes catalog + storage permissions). Test with `catalog.list_namespaces()`.

### 403 Forbidden

**Error:** `"403 Forbidden"` on data files  
**Cause:** Token lacks storage permissions.  
**Solution:** Token needs both R2 Data Catalog + R2 Storage Bucket Item permissions.

### Token Rotation Issues

**Error:** New token fails after rotation.  
**Solution:** Create new token → test in staging → update prod → monitor 24h → revoke old.

