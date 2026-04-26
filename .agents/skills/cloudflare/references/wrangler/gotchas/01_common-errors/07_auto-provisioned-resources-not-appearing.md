### "Auto-provisioned resources not appearing"

**Cause:** IDs written back to config on first deploy, but config not reloaded
**Solution:** After first deploy with auto-provisioning, config file is updated with IDs. Commit the updated config. On subsequent deploys, existing resources are reused.

