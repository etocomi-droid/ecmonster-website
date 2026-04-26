### "deleted_classes Destroys Data"

**Problem:** Migration deleted all data  
**Cause:** `deleted_classes` migration immediately destroys all DO instances and data  
**Solution:** Test with `--dry-run`; use `transferred_classes` to preserve data during moves

