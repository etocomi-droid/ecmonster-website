## wrangler.jsonc Setup

```jsonc
{
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",  // Use current date for new projects
  "observability": {
    "enabled": true  // Enables Workflows dashboard + structured logs
  },
  "workflows": [
    {
      "name": "my-workflow",           // Workflow name
      "binding": "MY_WORKFLOW",        // Env binding
      "class_name": "MyWorkflow"      // TS class name
      // "script_name": "other-worker" // For cross-script calls
    }
  ],
  "limits": {
    "cpu_ms": 300000  // 5 min max (default 30s)
  }
}
```

