## Worker Formats
```capnp
# ES Modules (recommended)
modules = [(name = "index.js", esModule = embed "src/index.js"), (name = "wasm.wasm", wasm = embed "build/module.wasm")]

# Service Worker (legacy)
serviceWorkerScript = embed "worker.js"

# CommonJS
(name = "legacy.js", commonJsModule = embed "legacy.js", namedExports = ["foo"])
```

