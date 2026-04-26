## Logging Configuration

**wrangler.jsonc**:
```jsonc
{
  "vars": {
    "SANDBOX_LOG_LEVEL": "debug",  // debug | info | warn | error (default: info)
    "SANDBOX_LOG_FORMAT": "pretty" // json | pretty (default: json)
  }
}
```

**Dev**: `debug` + `pretty`. **Production**: `info`/`warn` + `json`.

