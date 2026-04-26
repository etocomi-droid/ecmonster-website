## Environment Overrides

Top-level → local dev, `env.preview` → preview, `env.production` → production

```jsonc
{
  "vars": { "API_URL": "http://localhost:8787" },
  "env": {
    "production": { "vars": { "API_URL": "https://api.example.com" } }
  }
}
```

**Note:** If overriding `vars`, `kv_namespaces`, `d1_databases`, etc., ALL must be redefined (non-inheritable)

