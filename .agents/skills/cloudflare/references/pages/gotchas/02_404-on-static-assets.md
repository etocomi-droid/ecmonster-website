## 404 on Static Assets

**Problem**: Static files not serving  
**Causes**: Build output dir misconfigured; Functions catching requests; Advanced mode missing `env.ASSETS.fetch()`  
**Solution**: Verify output dir, add exclusions to `_routes.json`, call `env.ASSETS.fetch()` in `_worker.js`

