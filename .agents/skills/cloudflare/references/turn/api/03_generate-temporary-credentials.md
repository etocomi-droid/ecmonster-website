## Generate Temporary Credentials

```
POST https://rtc.live.cloudflare.com/v1/turn/keys/{key_id}/credentials/generate
Authorization: Bearer {key_secret}
Content-Type: application/json

{
  "ttl": 86400
}
```

### Credential Constraints

| Parameter | Min | Max | Default | Notes |
|-----------|-----|-----|---------|-------|
| ttl | 1 | 172800 (48hrs) | varies | API rejects values >172800 |

**CRITICAL**: Maximum TTL is 48 hours (172800 seconds). API will reject requests exceeding this limit.

### Response Schema

```json
{
  "iceServers": {
    "urls": [
      "stun:stun.cloudflare.com:3478",
      "turn:turn.cloudflare.com:3478?transport=udp",
      "turn:turn.cloudflare.com:3478?transport=tcp",
      "turn:turn.cloudflare.com:53?transport=udp",
      "turn:turn.cloudflare.com:80?transport=tcp",
      "turns:turn.cloudflare.com:5349?transport=tcp",
      "turns:turn.cloudflare.com:443?transport=tcp"
    ],
    "username": "1738035200:user123",
    "credential": "base64encodedhmac=="
  }
}
```

**Port 53 Warning**: Filter port 53 URLs for browser clients—blocked by Chrome/Firefox. See [gotchas.md](./gotchas.md#using-port-53-in-browsers).

