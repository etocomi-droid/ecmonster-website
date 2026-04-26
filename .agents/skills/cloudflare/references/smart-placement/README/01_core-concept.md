## Core Concept

Smart Placement automatically analyzes Worker request duration across Cloudflare's global network and intelligently routes requests to optimal data center locations. Instead of defaulting to the location closest to the end user, Smart Placement can forward requests to locations closer to backend infrastructure when this reduces overall request duration.

### When to Use

**Enable Smart Placement when:**
- Worker makes multiple round trips to backend services/databases
- Backend infrastructure is geographically concentrated
- Request duration dominated by backend latency rather than network latency from user
- Running backend logic in Workers (APIs, data aggregation, SSR with DB calls)
- Worker uses `fetch` handler (not RPC methods)

**Do NOT enable for:**
- Workers serving only static content or cached responses
- Workers without significant backend communication
- Pure edge logic (auth checks, redirects, simple transformations)
- Workers without fetch event handlers
- Workers with RPC methods or named entrypoints (only `fetch` handlers are affected)
- Pages/Assets Workers with `run_worker_first = true` (degrades asset serving)

### Decision Tree

```
Does your Worker have a fetch handler?
├─ No → Smart Placement won't work (skip)
└─ Yes
   │
   Does it make multiple backend calls (DB/API)?
   ├─ No → Don't enable (won't help)
   └─ Yes
      │
      Is backend geographically concentrated?
      ├─ No (globally distributed) → Probably won't help
      └─ Yes or uncertain
         │
         Does it serve static assets with run_worker_first=true?
         ├─ Yes → Don't enable (will hurt performance)
         └─ No → Enable Smart Placement
            │
            After 15min, check placement_status
            ├─ SUCCESS → Monitor metrics
            ├─ INSUFFICIENT_INVOCATIONS → Need more traffic
            └─ UNSUPPORTED_APPLICATION → Disable (hurting performance)
```

### Key Architecture Pattern

**Recommended:** Split full-stack applications into separate Workers:
```
User → Frontend Worker (at edge, close to user)
         ↓ Service Binding
       Backend Worker (Smart Placement enabled, close to DB/API)
         ↓
       Database/Backend Service
```

This maintains fast, reactive frontends while optimizing backend latency.

