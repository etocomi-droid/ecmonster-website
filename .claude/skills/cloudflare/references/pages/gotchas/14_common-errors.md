## Common Errors

### "Module not found"
**Cause**: Dependencies not bundled or build output incorrect  
**Solution**: Check build output directory, ensure dependencies bundled

### "Binding not found"
**Cause**: Binding not configured or types out of sync  
**Solution**: Verify wrangler.jsonc, run `npx wrangler types`

### "Request exceeded CPU limit"
**Cause**: Code execution too slow or heavy compute  
**Solution**: Optimize hot paths, upgrade to Workers Paid

### "Script too large"
**Cause**: Bundle size exceeds limit  
**Solution**: Tree-shake, use dynamic imports, code-split

### "Too many subrequests"
**Cause**: Exceeded 50 subrequest limit  
**Solution**: Batch or reduce fetch calls

### "KV key not found"
**Cause**: Key doesn't exist or wrong namespace  
**Solution**: Check namespace matches environment

### "D1 error"
**Cause**: Wrong database_id or missing migrations  
**Solution**: Verify config, run `wrangler d1 migrations list`

