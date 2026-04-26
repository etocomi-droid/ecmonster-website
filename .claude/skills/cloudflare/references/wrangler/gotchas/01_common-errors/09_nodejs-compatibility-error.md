### "Node.js compatibility error"

**Cause:** Missing Node.js compatibility flag
**Solution:** Some bindings (Hyperdrive with `pg`) require:
```jsonc
{ "compatibility_flags": ["nodejs_compat_v2"] }
```

