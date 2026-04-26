## Troubleshooting

### Authentication Issues
```bash
wrangler logout
wrangler login
wrangler whoami
```

### Configuration Errors
```bash
wrangler check  # Validate config
```
Use wrangler.jsonc with `$schema` for validation.

### Binding Not Available
- Check binding exists in config
- For environments, ensure binding defined for that env
- Local dev: some bindings need `--remote`

### Deployment Failures
```bash
wrangler tail              # Check logs
wrangler deploy --dry-run  # Validate
wrangler whoami            # Check account limits
```

### Local Development Issues
```bash
rm -rf .wrangler/state     # Clear local state
wrangler dev --remote      # Use remote bindings
wrangler dev --persist-to ./local-state  # Custom persist location
wrangler dev --inspector-port 9229  # Enable debugging
```

### Testing Issues
```bash
# If tests hang, ensure dispose() is called
worker.dispose()  // Always cleanup

# If bindings don't work in tests
const worker = await startWorker({ 
  config: "wrangler.jsonc",
  remote: "minimal"  // Use remote bindings
});
```

