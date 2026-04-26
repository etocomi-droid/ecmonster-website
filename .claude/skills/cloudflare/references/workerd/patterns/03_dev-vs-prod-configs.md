## Dev vs Prod Configs
```capnp
# Use parameter bindings for env-specific config
const baseWorker :Workerd.Worker = (
  modules = [(name = "index.js", esModule = embed "src/index.js")],
  compatibilityDate = "2024-01-15",
  bindings = [(name = "API_URL", parameter = (type = text))]
);

const prodWorker :Workerd.Worker = (
  inherit = "base-service",
  bindings = [(name = "API_URL", text = "https://api.prod.com")]
);
```

