## SendEmail Binding

Outbound email API for transactional messages.

### Configuration

```jsonc
// wrangler.jsonc
{
  "send_email": [
    { "name": "EMAIL" }
  ]
}
```

### TypeScript Types

```typescript
interface Env {
  EMAIL: SendEmail;
}

interface SendEmail {
  send(message: EmailMessage): Promise<void>;
}

interface EmailMessage {
  from: string | { name?: string; email: string };
  to: string | { name?: string; email: string } | Array<string | { name?: string; email: string }>;
  subject: string;
  text?: string;
  html?: string;
  headers?: Headers;
  reply_to?: string | { name?: string; email: string };
}
```

### Send Email Example

```typescript
interface Env {
  EMAIL: SendEmail;
}

export default {
  async fetch(request, env, ctx): Promise<Response> {
    await env.EMAIL.send({
      from: { name: "Acme Corp", email: "noreply@yourdomain.com" },
      to: [
        { name: "Alice", email: "alice@example.com" },
        "bob@example.com"
      ],
      subject: "Your order #12345 has shipped",
      text: "Track your package at: https://track.example.com/12345",
      html: "<p>Track your package at: <a href='https://track.example.com/12345'>View tracking</a></p>",
      reply_to: { name: "Support", email: "support@yourdomain.com" }
    });
    
    return new Response("Email sent");
  }
} satisfies ExportedHandler<Env>;
```

### SendEmail Constraints

- **From address**: Must be on verified domain (your domain with Email Routing enabled)
- **Volume limits**: Transactional only, no bulk/marketing email
- **Rate limits**: 100 emails/minute on Free plan, higher on Paid
- **No attachments**: Use links to hosted files instead
- **No DKIM control**: Cloudflare signs automatically

