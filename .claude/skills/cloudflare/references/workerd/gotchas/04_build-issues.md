## Build Issues

**Problem:** Cap'n Proto syntax errors
**Cause:** Invalid config or missing schema
**Solution:** Install capnproto tools, validate: `capnp compile -I. config.capnp`

**Problem:** Embed path not found
**Cause:** Path relative to config file
**Solution:** Use correct relative path or absolute path

**Problem:** V8 flags cause crashes
**Cause:** Unsafe V8 flags
**Solution:** ⚠️ V8 flags unsupported in production. Test thoroughly before use.

