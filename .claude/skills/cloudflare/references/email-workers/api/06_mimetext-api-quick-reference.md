## mimetext API Quick Reference

mimetext v3.0.27 composes outgoing emails.

```typescript
import { createMimeMessage } from 'mimetext';

const msg = createMimeMessage();

// Sender
msg.setSender({ name: 'John Doe', addr: 'john@example.com' });

// Recipients
msg.setRecipient('alice@example.com');
msg.setRecipients(['bob@example.com', 'carol@example.com']);
msg.setCc('manager@example.com');
msg.setBcc(['audit@example.com']);

// Headers
msg.setSubject('Meeting Notes');
msg.setHeader('In-Reply-To', '<previous-message-id>');
msg.setHeader('References', '<msg1> <msg2>');
msg.setHeader('Message-ID', `<${crypto.randomUUID()}@example.com>`);

// Content
msg.addMessage({
  contentType: 'text/plain',
  data: 'Plain text content'
});

msg.addMessage({
  contentType: 'text/html',
  data: '<p>HTML content</p>'
});

// Attachments
msg.addAttachment({
  filename: 'report.pdf',
  contentType: 'application/pdf',
  data: pdfBuffer // Uint8Array or base64 string
});

// Generate raw MIME
const raw = msg.asRaw(); // Returns string
```

