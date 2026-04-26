## Local Dev Issues

**Problem**: Dev server errors or bindings don't work  
**Causes**: Port conflict; bindings not passed; local vs HTTPS differences  
**Solution**: Use `--port=3000`; pass bindings via CLI or wrangler.jsonc; account for HTTP/HTTPS differences

