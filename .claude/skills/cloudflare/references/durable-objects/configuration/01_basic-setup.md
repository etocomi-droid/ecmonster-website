## Basic Setup

```jsonc
{
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",  // Use latest; ≥2024-04-03 for RPC
  "durable_objects": {
    "bindings": [
      { 
        "name": "MY_DO",                // Env binding name
        "class_name": "MyDO"            // Class exported from this worker
      },
      { 
        "name": "EXTERNAL",             // Access DO from another worker
        "class_name": "ExternalDO", 
        "script_name": "other-worker"
      }
    ]
  },
  "migrations": [
    { "tag": "v1", "new_sqlite_classes": ["MyDO"] }  // Prefer SQLite
  ]
}
```

