## Services
**Worker**: Run JS/Wasm code
```capnp
(name = "api", worker = (
  modules = [(name = "index.js", esModule = embed "index.js")],
  compatibilityDate = "2024-01-15",
  bindings = [...]
))
```

**Network**: Internet access
```capnp
(name = "internet", network = (allow = ["public"], tlsOptions = (trustBrowserCas = true)))
```

**External**: Reverse proxy
```capnp
(name = "backend", external = (address = "api.com:443", http = (style = tls)))
```

**Disk**: Static files
```capnp
(name = "assets", disk = (path = "/var/www", writable = false))
```

