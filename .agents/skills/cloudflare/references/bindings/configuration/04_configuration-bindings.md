## Configuration Bindings

```jsonc
{
  "vars": {
    "API_URL": "https://api.example.com",
    "MAX_RETRIES": "3"
  },
  "text_blobs": { "MY_TEXT": "./data/template.html" },
  "data_blobs": { "MY_DATA": "./data/config.bin" },
  "wasm_modules": { "MY_WASM": "./build/module.wasm" }
}
```

**Secrets (never in config):**
```bash
npx wrangler secret put API_KEY
```

