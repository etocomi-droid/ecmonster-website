## Sockets
```capnp
(name = "http", address = "*:8080", http = (), service = "main")
(name = "https", address = "*:443", https = (options = (), tlsOptions = (keypair = (...))), service = "main")
(name = "app", address = "unix:/tmp/app.sock", http = (), service = "main")
```

