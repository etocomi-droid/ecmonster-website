## Durable Objects
```capnp
const worker :Workerd.Worker = (
  modules = [(name = "index.js", esModule = embed "index.js"), (name = "room.js", esModule = embed "room.js")],
  compatibilityDate = "2024-01-15",
  bindings = [(name = "ROOMS", durableObjectNamespace = "Room")],
  durableObjectNamespaces = [(className = "Room", uniqueKey = "v1")],
  durableObjectStorage = (localDisk = "/var/do")
);
```

