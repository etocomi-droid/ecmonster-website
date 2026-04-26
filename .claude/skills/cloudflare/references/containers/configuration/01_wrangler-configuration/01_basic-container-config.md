### Basic Container Config

```jsonc
{
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2026-01-10",
  "containers": [
    {
      "class_name": "MyContainer",
      "image": "./Dockerfile",  // Path to Dockerfile or directory with Dockerfile
      "instance_type": "standard-1",  // Predefined or custom (see below)
      "max_instances": 10
    }
  ],
  "durable_objects": {
    "bindings": [
      {
        "name": "MY_CONTAINER",
        "class_name": "MyContainer"
      }
    ]
  },
  "migrations": [
    {
      "tag": "v1",
      "new_sqlite_classes": ["MyContainer"]  // Must use new_sqlite_classes
    }
  ]
}
```

Key config requirements:
- `image` - Path to Dockerfile or directory containing Dockerfile
- `class_name` - Must match Container class export name
- `max_instances` - Max concurrent container instances
- Must configure Durable Objects binding AND migrations

