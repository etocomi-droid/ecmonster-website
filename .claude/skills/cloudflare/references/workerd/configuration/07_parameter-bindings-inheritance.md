## Parameter Bindings (Inheritance)
```capnp
const base :Workerd.Worker = (
  modules = [...], compatibilityDate = "2024-01-15",
  bindings = [(name = "API_URL", parameter = (type = text)), (name = "DB", parameter = (type = service))]
);

const derived :Workerd.Worker = (
  inherit = "base-service",
  bindings = [(name = "API_URL", text = "https://api.com"), (name = "DB", service = "postgres")]
);
```

