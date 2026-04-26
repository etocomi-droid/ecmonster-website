## Worker Runtime API

### Email Handler Interface

```typescript
interface ExportedHandler<Env = unknown> {
  email?(message: ForwardableEmailMessage, env: Env, ctx: ExecutionContext): void | Promise<void>;
}
```

### ForwardableEmailMessage

Main interface for incoming emails:

```typescript
interface ForwardableEmailMessage {
  readonly from: string;          // Envelope sender (e.g., "sender@example.com")
  readonly to: string;             // Envelope recipient (e.g., "you@yourdomain.com")
  readonly headers: Headers;       // Web API Headers object
  readonly raw: ReadableStream;    // Raw MIME message stream
  
  setReject(reason: string): void;
  forward(rcptTo: string, headers?: Headers): Promise<void>;
}
```

**Key Properties:**

| Property | Type | Description |
|----------|------|-------------|
| `from` | `string` | Envelope sender (MAIL FROM), not header From |
| `to` | `string` | Envelope recipient (RCPT TO), not header To |
| `headers` | `Headers` | Email headers (Subject, From, To, etc.) |
| `raw` | `ReadableStream` | Raw MIME message (consume once only) |

**Methods:**

- `setReject(reason)`: Reject email with bounce message
- `forward(rcptTo, headers?)`: Forward to verified destination, optionally add headers

### Headers Object

Standard Web API Headers interface:

```typescript
// Access headers
const subject = message.headers.get("subject");
const from = message.headers.get("from");
const messageId = message.headers.get("message-id");

// Check spam score
const spamScore = parseFloat(message.headers.get("x-cf-spamh-score") || "0");
if (spamScore > 5) {
  message.setReject("Spam detected");
}
```

### Common Headers

`subject`, `from`, `to`, `x-cf-spamh-score` (spam score), `message-id` (deduplication), `dkim-signature` (auth)

### Envelope vs Header Addresses

**Critical distinction:**

```typescript
// Envelope addresses (routing, auth checks)
message.from // "bounce@sender.com" (actual sender)
message.to   // "you@yourdomain.com" (your address)

// Header addresses (display, user-facing)
message.headers.get("from") // "Alice <alice@sender.com>"
message.headers.get("to")   // "Bob <you@yourdomain.com>"
```

**Use envelope addresses for:**
- Authentication/SPF checks
- Routing decisions
- Bounce handling

**Use header addresses for:**
- Display to users
- Reply-To logic
- User-facing filtering

