## Bindings
Bindings expose resources to workers. ES modules: `env.BINDING`, Service workers: globals.

### Primitive Types
```capnp
(name = "API_KEY", text = "secret")                    # String
(name = "CONFIG", json = '{"key":"val"}')              # Parsed JSON
(name = "DATA", data = embed "data.bin")               # ArrayBuffer
(name = "DATABASE_URL", fromEnvironment = "DB_URL")    # System env var
```

### Service Binding
```capnp
(name = "AUTH", service = "auth-worker")               # Basic
(name = "API", service = (
  name = "backend",
  entrypoint = "adminApi",                             # Named export
  props = (json = '{"role":"admin"}')                  # ctx.props
))
```

### Storage
```capnp
(name = "CACHE", kvNamespace = "kv-service")           # KV
(name = "STORAGE", r2Bucket = "r2-service")            # R2
(name = "ROOMS", durableObjectNamespace = (
  serviceName = "room-service",
  className = "Room"
))
(name = "FAST", memoryCache = (
  id = "cache-id",
  limits = (maxKeys = 1000, maxValueSize = 1048576)
))
```

### Other
```capnp
(name = "TASKS", queue = "queue-service")
(name = "ANALYTICS", analyticsEngine = "analytics")
(name = "LOADER", workerLoader = (id = "dynamic"))
(name = "KEY", cryptoKey = (format = raw, algorithm = (name = "HMAC", hash = "SHA-256"), keyData = embed "key.bin", usages = [sign, verify], extractable = false))
(name = "TRACED", wrapped = (moduleName = "tracing", entrypoint = "makeTracer", innerBindings = [(name = "backend", service = "backend")]))
```

