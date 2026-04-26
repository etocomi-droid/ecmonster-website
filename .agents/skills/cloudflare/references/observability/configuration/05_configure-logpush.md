### Configure Logpush

Send logs to external storage (S3, R2, GCS, Azure, Datadog, etc.). Requires Business/Enterprise plan.

**Via Dashboard**:
1. Navigate to Analytics → Logs → Logpush
2. Select destination type
3. Provide credentials and bucket/endpoint
4. Choose dataset (e.g., Workers Trace Events)
5. Configure filters and fields

**Via API**:
```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/{account_id}/logpush/jobs" \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "workers-logs-to-s3",
    "destination_conf": "s3://my-bucket/logs?region=us-east-1",
    "dataset": "workers_trace_events",
    "enabled": true,
    "frequency": "high",
    "filter": "{\"where\":{\"and\":[{\"key\":\"ScriptName\",\"operator\":\"eq\",\"value\":\"my-worker\"}]}}"
  }'
```

