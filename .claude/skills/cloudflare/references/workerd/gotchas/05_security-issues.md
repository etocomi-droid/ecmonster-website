## Security Issues

**Problem:** Hardcoded secrets in config
**Cause:** `text` binding with secret value
**Solution:** Use `fromEnvironment` to load from env vars

**Problem:** Overly broad network access
**Cause:** `network = (allow = ["*"])`
**Solution:** Restrict to `allow = ["public"]` or specific hosts

**Problem:** Extractable crypto keys
**Cause:** `cryptoKey = (extractable = true, ...)`
**Solution:** Set `extractable = false` unless export required

