## Event Notifications

```jsonc
// wrangler.jsonc
{
  "r2_buckets": [
    {
      "binding": "MY_BUCKET",
      "bucket_name": "my-bucket",
      "event_notifications": [
        {
          "queue": "r2-events",
          "actions": ["PutObject", "DeleteObject", "CompleteMultipartUpload"]
        }
      ]
    }
  ],
  "queues": {
    "producers": [{ "binding": "R2_EVENTS", "queue": "r2-events" }],
    "consumers": [{ "queue": "r2-events", "max_batch_size": 10 }]
  }
}
```

