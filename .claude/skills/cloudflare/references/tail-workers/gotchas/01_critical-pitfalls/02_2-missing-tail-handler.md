### 2. Missing `tail()` Handler

**Problem:** Producer deployment fails  
**Cause:** Worker in `tail_consumers` doesn't export `tail()` handler  
**Solution:** Ensure `export default { async tail(events, env, ctx) { ... } }`

