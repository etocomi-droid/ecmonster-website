## When NOT to Use Smart Placement

- Workers serving only static content or cached responses
- Workers without significant backend communication
- Pure edge logic (auth checks, redirects, simple transformations)
- Workers without fetch event handlers
- Pages/Assets Workers with `run_worker_first = true`
- Workers using RPC methods instead of fetch handlers

These scenarios won't benefit and may perform worse with Smart Placement.
