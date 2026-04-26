## Compatibility Changes

**Problem:** Breaking changes after compat date update
**Cause:** New flags enabled between dates
**Solution:** Review [compat dates docs](https://developers.cloudflare.com/workers/configuration/compatibility-dates/), test locally first

**Problem:** "Compatibility date not supported"
**Cause:** Workerd version older than compat date
**Solution:** Update workerd binary (version = max compat date supported)

