## Local Development

**Recommended:** Use Wrangler
```bash
wrangler dev  # Uses workerd internally
```

**Direct workerd:**
```bash
workerd serve config.capnp --socket-addr http=*:3000 --verbose
```

**Environment variables:**
```capnp
bindings = [(name = "DATABASE_URL", fromEnvironment = "DATABASE_URL")]
```

