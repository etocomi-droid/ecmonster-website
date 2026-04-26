## Consumer Configuration (Push-based)

**wrangler.jsonc:**
```jsonc
{
  "queues": {
    "consumers": [
      {
        "queue": "my-queue-name",
        "max_batch_size": 10,           // 1-100, default 10
        "max_batch_timeout": 5,         // 0-60s, default 5
        "max_retries": 3,               // default 3, max 100
        "dead_letter_queue": "my-dlq",  // optional
        "retry_delay": 300              // optional: delay retries in seconds
      }
    ]
  }
}
```

