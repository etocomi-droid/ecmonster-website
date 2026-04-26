## HTTP Reverse Proxy
```capnp
services = [
  (name = "proxy", worker = (serviceWorkerScript = embed "proxy.js", compatibilityDate = "2024-01-15", bindings = [(name = "BACKEND", service = "backend")])),
  (name = "backend", external = (address = "internal:8080", http = ()))
]
```

