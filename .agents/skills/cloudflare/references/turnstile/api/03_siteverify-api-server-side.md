## Siteverify API (Server-Side)

**Endpoint:** `https://challenges.cloudflare.com/turnstile/v0/siteverify`

### Request

**Method:** POST  
**Content-Type:** `application/json` or `application/x-www-form-urlencoded`

```typescript
interface SiteverifyRequest {
  secret: string;    // Your secret key (never expose client-side)
  response: string;  // Token from cf-turnstile-response
  remoteip?: string; // User's IP (optional but recommended)
  idempotency_key?: string; // Unique key for idempotent validation
}
```

**Example:**
```javascript
// Cloudflare Workers
const result = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    secret: env.TURNSTILE_SECRET,
    response: token,
    remoteip: request.headers.get('CF-Connecting-IP')
  })
});
const data = await result.json();
```

### Response

```typescript
interface SiteverifyResponse {
  success: boolean;           // Validation result
  challenge_ts?: string;      // ISO timestamp of challenge
  hostname?: string;          // Hostname where widget was solved
  'error-codes'?: string[];   // Error codes if success=false
  action?: string;            // Action name from widget config
  cdata?: string;             // Custom data from widget config
}
```

**Example Success:**
```json
{
  "success": true,
  "challenge_ts": "2024-01-15T10:30:00Z",
  "hostname": "example.com",
  "action": "login",
  "cdata": "user123"
}
```

**Example Failure:**
```json
{
  "success": false,
  "error-codes": ["timeout-or-duplicate"]
}
```

