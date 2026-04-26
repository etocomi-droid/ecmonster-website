## Consumer Configuration (Pull-based)

**wrangler.jsonc:**
```jsonc
{
  "queues": {
    "consumers": [
      {
        "queue": "my-queue-name",
        "type": "http_pull",
        "visibility_timeout_ms": 5000,  // default 30000, max 12h
        "max_retries": 5,
        "dead_letter_queue": "my-dlq"
      }
    ]
  }
}
```

