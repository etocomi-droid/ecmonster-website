## SendEmail Binding Types

```jsonc
{
  "send_email": [
    { "name": "EMAIL" },  // Type 1: Any verified address
    { "name": "LOGS", "destination_address": "logs@example.com" },  // Type 2: Single dest
    { "name": "TEAM", "allowed_destination_addresses": ["a@ex.com", "b@ex.com"] },  // Type 3: Dest allowlist
    { "name": "NOREPLY", "allowed_sender_addresses": ["noreply@ex.com"] }  // Type 4: Sender allowlist
  ]
}
```

