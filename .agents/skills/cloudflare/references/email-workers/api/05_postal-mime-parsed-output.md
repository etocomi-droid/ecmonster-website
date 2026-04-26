## postal-mime Parsed Output

postal-mime v2.7.3 parses incoming emails into structured data.

```typescript
interface ParsedEmail {
  headers: Array<{ key: string; value: string }>;
  from: { name: string; address: string } | null;
  to: Array<{ name: string; address: string }> | { name: string; address: string } | null;
  cc: Array<{ name: string; address: string }> | null;
  bcc: Array<{ name: string; address: string }> | null;
  subject: string;
  messageId: string | null;
  inReplyTo: string | null;
  references: string | null;
  date: string | null;
  html: string | null;
  text: string | null;
  attachments: Array<{
    filename: string;
    mimeType: string;
    disposition: string | null;
    related: boolean;
    contentId: string | null;
    content: Uint8Array;
  }>;
}
```

### Usage

```typescript
import PostalMime from 'postal-mime';

const buffer = await new Response(message.raw).arrayBuffer();
const email = await PostalMime.parse(buffer);

console.log(email.subject);
console.log(email.from?.address);
console.log(email.text);
console.log(email.attachments.length);
```

