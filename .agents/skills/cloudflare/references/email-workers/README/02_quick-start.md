## Quick Start

### Minimal ES Modules Handler

```typescript
export default {
  async email(message, env, ctx) {
    // Reject spam
    if (message.from.includes('spam.com')) {
      message.setReject('Blocked');
      return;
    }
    
    // Forward to inbox
    await message.forward('inbox@example.com');
  }
};
```

### Core Operations

| Operation | Method | Use Case |
|-----------|--------|----------|
| Forward | `message.forward(to, headers?)` | Route to verified destination |
| Reject | `message.setReject(reason)` | Block with SMTP error |
| Reply | `message.reply(emailMessage)` | Auto-respond with threading |
| Parse | postal-mime library | Extract subject, body, attachments |

