## Logging & Debugging
```capnp
logging = (structuredLogging = true, stdoutPrefix = "OUT: ", stderrPrefix = "ERR: ")
v8Flags = ["--expose-gc", "--max-old-space-size=2048"]  # ⚠️ Unsupported in production
```

See [patterns.md](./patterns.md) for multi-service examples, [gotchas.md](./gotchas.md) for config errors.
