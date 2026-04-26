## Parsing

### Address Parsing

```typescript
const email = await PostalMime.parse(buffer);
const fromAddress = email.from?.address || 'unknown';
const toAddresses = Array.isArray(email.to) ? email.to.map(t => t.address) : [email.to?.address];
```

### Character Encoding

Let postal-mime handle decoding - `email.subject`, `email.text`, `email.html` are UTF-8.

