## EmailMessage Constructor

```typescript
import { EmailMessage } from 'cloudflare:email';

new EmailMessage(from: string, to: string, raw: ReadableStream | string)
```

Used for sending emails (replies or via SendEmail binding). Domain must be verified.

