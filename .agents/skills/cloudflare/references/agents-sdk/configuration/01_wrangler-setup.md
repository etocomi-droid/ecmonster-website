## Wrangler Setup

```jsonc
{
  "name": "my-agents-app",
  "durable_objects": {
    "bindings": [
      {"name": "MyAgent", "class_name": "MyAgent"}
    ]
  },
  "migrations": [
    {"tag": "v1", "new_sqlite_classes": ["MyAgent"]}
  ],
  "ai": {
    "binding": "AI"
  }
}
```

