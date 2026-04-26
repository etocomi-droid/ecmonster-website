## Auto-Reply with Threading

```typescript
import { EmailMessage } from 'cloudflare:email';
import { createMimeMessage } from 'mimetext';

const msg = createMimeMessage();
msg.setSender({ addr: 'support@example.com' });
msg.setRecipient(message.from);
msg.setSubject(`Re: ${message.headers.get('Subject')}`);
msg.setHeader('In-Reply-To', message.headers.get('Message-ID') || '');
msg.addMessage({ contentType: 'text/plain', data: 'Thank you. We will respond.' });

await message.reply(new EmailMessage('support@example.com', message.from, msg.asRaw()));
```

