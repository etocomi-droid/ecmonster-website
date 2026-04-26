## wrangler.jsonc

```jsonc
{
  "name": "email-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-27",
  "send_email": [
    { "name": "EMAIL" },                                    // Unrestricted
    { "name": "EMAIL_LOGS", "destination_address": "logs@example.com" },  // Single dest
    { "name": "EMAIL_TEAM", "allowed_destination_addresses": ["a@ex.com", "b@ex.com"] },
    { "name": "EMAIL_NOREPLY", "allowed_sender_addresses": ["noreply@ex.com"] }
  ],
  "kv_namespaces": [{ "binding": "ARCHIVE", "id": "xxx" }],
  "r2_buckets": [{ "binding": "ATTACHMENTS", "bucket_name": "email-attachments" }],
  "vars": { "WEBHOOK_URL": "https://hooks.example.com" }
}
```

