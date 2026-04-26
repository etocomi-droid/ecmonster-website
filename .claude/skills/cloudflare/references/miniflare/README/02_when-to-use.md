## When to Use

**Decision tree for testing Workers:**

```
Need to test Workers?
│
├─ Unit tests for business logic only?
│  └─ getPlatformProxy (Vitest/Jest) → [patterns.md](./patterns.md#getplatformproxy)
│     Fast, no HTTP, direct binding access
│
├─ Integration tests with full runtime?
│  ├─ Single Worker?
│  │  └─ Miniflare API → [Quick Start](#quick-start)
│  │     Full control, programmatic access
│  │
│  ├─ Multiple Workers + service bindings?
│  │  └─ Miniflare workers array → [configuration.md](./configuration.md#multiple-workers)
│  │     Shared storage, inter-worker calls
│  │
│  └─ Vitest test runner integration?
│     └─ vitest-pool-workers → [patterns.md](./patterns.md#vitest-pool-workers)
│        Full Workers env in Vitest
│
└─ Local dev server?
   └─ wrangler dev (not Miniflare)
      Hot reload, automatic config
```

**Use Miniflare for:**
- Integration tests with full Worker runtime
- Testing bindings/storage locally
- Multiple Workers with service bindings
- Programmatic event dispatch (fetch, queue, scheduled)

**Use getPlatformProxy for:**
- Fast unit tests of business logic
- Testing without HTTP overhead
- Vitest/Jest environments

**Use Wrangler for:**
- Local development workflow
- Production deployments

