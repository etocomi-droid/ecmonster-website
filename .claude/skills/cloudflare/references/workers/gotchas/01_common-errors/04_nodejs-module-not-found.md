### "Node.js module not found"

**Cause:** Node.js built-ins not available by default  
**Solution:** Use Workers APIs (e.g., R2 for file storage) or enable Node.js compat with `"compatibility_flags": ["nodejs_compat_v2"]`

