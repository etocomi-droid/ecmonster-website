## Subject-Based Routing

```typescript
const subject = (message.headers.get('Subject') || '').toLowerCase();
if (subject.includes('billing')) await message.forward('billing@example.com');
else if (subject.includes('support')) await message.forward('support@example.com');
else await message.forward('general@example.com');
```

