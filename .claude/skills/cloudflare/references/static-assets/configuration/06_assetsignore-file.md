### .assetsignore File

Exclude files from upload using `.assetsignore` (same syntax as `.gitignore`):

```
# .assetsignore
_worker.js
*.map
*.md
node_modules/
.git/
```

**Common patterns:**

- `_worker.js` - Exclude Worker code from assets
- `*.map` - Exclude source maps
- `*.md` - Exclude markdown files
- Development artifacts

