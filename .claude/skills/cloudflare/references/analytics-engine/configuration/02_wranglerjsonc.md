## wrangler.jsonc

```jsonc
{
  "name": "my-worker",
  "analytics_engine_datasets": [
    { "binding": "ANALYTICS", "dataset": "my_events" }
  ]
}
```

Multiple datasets for separate concerns:
```jsonc
{
  "analytics_engine_datasets": [
    { "binding": "API_ANALYTICS", "dataset": "api_requests" },
    { "binding": "USER_EVENTS", "dataset": "user_activity" }
  ]
}
```

