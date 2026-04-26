## Multi-Service Architecture
```capnp
const config :Workerd.Config = (
  services = [
    (name = "frontend", worker = (
      modules = [(name = "index.js", esModule = embed "frontend/index.js")],
      compatibilityDate = "2024-01-15",
      bindings = [(name = "API", service = "api")]
    )),
    (name = "api", worker = (
      modules = [(name = "index.js", esModule = embed "api/index.js")],
      compatibilityDate = "2024-01-15",
      bindings = [(name = "DB", service = "postgres"), (name = "CACHE", kvNamespace = "kv")]
    )),
    (name = "postgres", external = (address = "db.internal:5432", http = ())),
    (name = "kv", disk = (path = "/var/kv", writable = true))
  ],
  sockets = [(name = "http", address = "*:8080", http = (), service = "frontend")]
);
```

