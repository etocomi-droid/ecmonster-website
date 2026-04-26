### "Cannot fetch in global scope"

**Cause:** Attempting to use fetch during module initialization  
**Solution:** Move fetch calls inside handler functions (fetch, scheduled, etc.) where they're allowed

