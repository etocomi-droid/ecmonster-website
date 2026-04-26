## ForwardableEmailMessage Interface

The main interface passed to email handlers.

```typescript
interface ForwardableEmailMessage {
  readonly from: string;        // Envelope MAIL FROM (SMTP sender)
  readonly to: string;          // Envelope RCPT TO (SMTP recipient)
  readonly headers: Headers;    // Web-standard Headers object
  readonly raw: ReadableStream; // Raw MIME message (single-use stream)
  readonly rawSize: number;     // Total message size in bytes
  
  setReject(reason: string): void;
  forward(rcptTo: string, headers?: Headers): Promise<void>;
  reply(message: EmailMessage): Promise<void>;
}
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `from` | string | Envelope sender (SMTP MAIL FROM) - use for security |
| `to` | string | Envelope recipient (SMTP RCPT TO) |
| `headers` | Headers | Message headers (Subject, Message-ID, etc.) |
| `raw` | ReadableStream | Raw MIME message (**single-use**, buffer first) |
| `rawSize` | number | Message size in bytes |

### Methods

#### setReject(reason: string): void

Reject with permanent SMTP 5xx error. Email not delivered, sender may receive bounce.

```typescript
if (blockList.includes(message.from)) {
  message.setReject('Sender blocked');
}
```

#### forward(rcptTo: string, headers?: Headers): Promise<void>

Forward to verified destination. Only `X-*` custom headers allowed.

```typescript
await message.forward('inbox@example.com');

// With custom headers
const h = new Headers();
h.set('X-Processed-By', 'worker');
await message.forward('inbox@example.com', h);
```

#### reply(message: EmailMessage): Promise<void>

Send a reply to the original sender (March 2025 feature).

```typescript
import { EmailMessage } from 'cloudflare:email';
import { createMimeMessage } from 'mimetext';

const msg = createMimeMessage();
msg.setSender({ name: 'Support', addr: 'support@example.com' });
msg.setRecipient(message.from);
msg.setSubject(`Re: ${message.headers.get('Subject')}`);
msg.setHeader('In-Reply-To', message.headers.get('Message-ID'));
msg.setHeader('References', message.headers.get('References') || '');
msg.addMessage({
  contentType: 'text/plain',
  data: 'Thank you for your message.'
});

await message.reply(new EmailMessage(
  'support@example.com',
  message.from,
  msg.asRaw()
));
```

**Requirements**:
- Incoming email needs valid DMARC
- Reply once per event, recipient = `message.from`
- Sender domain = receiving domain, with DMARC/SPF/DKIM
- Max 100 `References` entries
- Threading: `In-Reply-To` (original Message-ID), `References`, new `Message-ID`

