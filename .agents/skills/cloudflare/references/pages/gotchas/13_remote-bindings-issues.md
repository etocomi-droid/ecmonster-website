## Remote Bindings Issues

### Accidentally Modified Production Data

**Problem**: Local dev with `--remote` altered production database/KV  
**Cause**: Remote bindings connect directly to production resources; writes are real  
**Solution**: 
- Use `--remote` only for read-heavy debugging
- Create separate preview environments for testing
- Never use `--remote` for write operations during development

### Remote Binding Auth Errors

**Problem**: `npx wrangler pages dev --remote` fails with "Unauthorized" or auth error  
**Cause**: Not logged in, session expired, or insufficient account permissions  
**Solution**: 
1. Run `npx wrangler login` to re-authenticate
2. Verify account has access to project and bindings
3. Check binding IDs match production configuration

### Slow Local Dev with Remote Bindings

**Problem**: Local dev server slow when using `--remote`  
**Cause**: Every request makes network calls to production bindings  
**Solution**: Use local bindings for development; reserve `--remote` for final validation

