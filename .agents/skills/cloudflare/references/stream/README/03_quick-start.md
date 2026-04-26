## Quick Start

**Upload video via API**
```bash
curl -X POST \
  "https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/copy" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/video.mp4"}'
```

**Embed player**
```html
<iframe
  src="https://customer-<CODE>.cloudflarestream.com/<VIDEO_ID>/iframe"
  style="border: none;"
  height="720" width="1280"
  allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;"
  allowfullscreen="true"
></iframe>
```

**Create live input**
```bash
curl -X POST \
  "https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"recording": {"mode": "automatic"}}'
```

