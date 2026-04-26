## Middleware Not Running

**Problem**: Middleware doesn't execute  
**Causes**: Wrong filename (not `_middleware.ts`); missing `onRequest` export; didn't call `next()`  
**Solution**: Rename file with underscore prefix; export handler; call `next()` or return Response

