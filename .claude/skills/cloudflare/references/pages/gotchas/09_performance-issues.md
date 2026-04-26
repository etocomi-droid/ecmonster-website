## Performance Issues

**Problem**: Slow responses or CPU limit errors  
**Causes**: Functions invoked for static assets; cold starts; 10ms CPU limit; large bundle  
**Solution**: Exclude static via `_routes.json`; optimize hot paths; keep bundle < 1MB

