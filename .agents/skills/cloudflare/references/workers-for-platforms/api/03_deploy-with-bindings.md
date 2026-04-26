## Deploy with Bindings
```bash
curl -X PUT ".../scripts/$SCRIPT_NAME" \
  -F 'metadata={
    "main_module": "worker.mjs",
    "bindings": [
      {"type": "kv_namespace", "name": "MY_KV", "namespace_id": "'$KV_ID'"}
    ],
    "tags": ["customer-123", "production"],
    "compatibility_date": "2026-01-01"  // Use current date for new projects
  };type=application/json' \
  -F 'worker.mjs=@worker.mjs;type=application/javascript+module'
```

