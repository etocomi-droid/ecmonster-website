### "Durable Object binding not working"

**Cause:** Missing script_name for external DOs
**Solution:** Always specify `script_name` for external Durable Objects:
```jsonc
{
  "durable_objects": {
    "bindings": [
      { "name": "MY_DO", "class_name": "MyDO", "script_name": "my-worker" }
    ]
  }
}
```

For local DOs in same Worker, `script_name` is optional.

