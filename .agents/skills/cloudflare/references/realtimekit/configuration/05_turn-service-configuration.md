## TURN Service Configuration

RealtimeKit can use Cloudflare's TURN service for connectivity through restrictive networks:

```jsonc
// wrangler.jsonc
{
  "vars": {
    "TURN_SERVICE_ID": "your_turn_service_id"
  }
  // Set secret: wrangler secret put TURN_SERVICE_TOKEN
}
```

TURN automatically configured when enabled in account - no client-side changes needed.

