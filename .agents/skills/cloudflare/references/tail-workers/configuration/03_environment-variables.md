## Environment Variables

Tail Workers use same binding syntax as regular Workers:

```jsonc
{
  "name": "my-tail-worker",
  "vars": {
    "LOG_ENDPOINT": "https://logs.example.com/ingest"
  },
  "kv_namespaces": [
    {
      "binding": "LOGS_KV",
      "id": "abc123..."
    }
  ]
}
```

