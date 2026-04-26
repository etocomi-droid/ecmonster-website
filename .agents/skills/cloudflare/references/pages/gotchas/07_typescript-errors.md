## TypeScript Errors

**Problem**: Type errors in Functions code  
**Causes**: Types not generated; Env interface doesn't match wrangler.jsonc  
**Solution**: Run `npx wrangler types --path='./functions/types.d.ts'`; update Env interface

