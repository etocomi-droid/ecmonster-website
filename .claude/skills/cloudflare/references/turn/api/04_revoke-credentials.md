## Revoke Credentials

```
POST https://rtc.live.cloudflare.com/v1/turn/keys/{key_id}/credentials/revoke
Authorization: Bearer {key_secret}
Content-Type: application/json

{
  "username": "1738035200:user123"
}
```

**Response**: 204 No Content

Billing stops immediately. Active connection drops after short delay (~seconds).

