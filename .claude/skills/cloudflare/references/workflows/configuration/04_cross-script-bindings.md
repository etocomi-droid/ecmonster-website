## Cross-Script Bindings

Worker A defines workflow. Worker B calls it by adding `script_name`:

```jsonc
// Worker B (caller)
{
  "workflows": [{
    "name": "billing-workflow",
    "binding": "BILLING",
    "script_name": "billing-worker"  // Points to Worker A
  }]
}
```

