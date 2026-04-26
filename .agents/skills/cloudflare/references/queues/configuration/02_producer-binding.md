## Producer Binding

**wrangler.jsonc:**
```jsonc
{
  "queues": {
    "producers": [
      {
        "queue": "my-queue-name",
        "binding": "MY_QUEUE",
        "delivery_delay": 60  // Optional: default delay in seconds
      }
    ]
  }
}
```

