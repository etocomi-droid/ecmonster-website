### "Workers Assets 404 errors"

**Cause:** Asset path mismatch or incorrect `html_handling`
**Solution:** 
- Check `assets.directory` points to correct build output
- Set `html_handling: "auto-trailing-slash"` for SPAs
- Use `not_found_handling: "single-page-application"` to serve index.html for 404s
```jsonc
{
  "assets": {
    "directory": "./dist",
    "html_handling": "auto-trailing-slash",
    "not_found_handling": "single-page-application"
  }
}
```

