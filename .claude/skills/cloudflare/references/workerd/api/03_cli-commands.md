## CLI Commands

```bash
workerd serve config.capnp [constantName]          # Start server
workerd serve config.capnp --socket-addr http=*:3000 --verbose
workerd compile config.capnp constantName -o binary  # Compile to binary
workerd test config.capnp [--test-only=test.js]    # Run tests
```

