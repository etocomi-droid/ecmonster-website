### "Local dev behavior differs from production"

**Cause:** Using local simulation instead of remote execution
**Solution:** Choose appropriate remote mode:
- `wrangler dev` (default): Local simulation, fast, limited accuracy
- `wrangler dev --remote`: Full remote execution, production-accurate, slower
- Use `remote: "minimal"` in tests for fast tests with real remote bindings

