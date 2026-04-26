## Common Errors

### "Stream upload failed" / Silent Truncation

**Cause:** Stream length unknown or Content-Length missing  
**Solution:** Buffer data or pass explicit Content-Length

### "Invalid credentials" / S3 SDK

**Cause:** Missing `region: 'auto'` in S3Client config  
**Solution:** Always set `region: 'auto'` for R2

### "Object not found"

**Cause:** Object key doesn't exist or was deleted  
**Solution:** Verify object key correct, check if object was deleted, ensure bucket correct

### "List compatibility error"

**Cause:** Missing or old compatibility_date, or flag not enabled  
**Solution:** Set `compatibility_date >= 2022-08-04` or enable `r2_list_honor_include` flag

### "Multipart upload failed"

**Cause:** Part sizes not uniform or incorrect part number  
**Solution:** Ensure uniform size except final part, verify part numbers start at 1
