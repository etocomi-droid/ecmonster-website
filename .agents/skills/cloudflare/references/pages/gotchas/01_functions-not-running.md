## Functions Not Running

**Problem**: Function endpoints return 404 or don't execute  
**Causes**: `_routes.json` excludes path; wrong file extension (`.jsx`/`.tsx`); Functions dir not at output root  
**Solution**: Check `_routes.json`, rename to `.ts`/`.js`, verify build output structure

