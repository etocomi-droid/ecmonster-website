## API Behavior

### setReject() vs throw

```typescript
// setReject() for SMTP rejection
if (blockList.includes(message.from)) { message.setReject('Blocked'); return; }

// throw for worker errors
if (!env.KV) throw new Error('KV not configured');
```

### forward() Only X-* Headers

```typescript
headers.set('X-Processed-By', 'worker');  // ✅ Works
headers.set('Subject', 'Modified');        // ❌ Dropped
```

### Reply Requires Verified Domain

```typescript
// Use same domain as receiving address
const receivingDomain = message.to.split('@')[1];
await message.reply(new EmailMessage(`noreply@${receivingDomain}`, message.from, rawMime));
```

