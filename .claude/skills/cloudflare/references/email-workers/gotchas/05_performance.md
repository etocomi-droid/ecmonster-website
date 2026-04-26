## Performance

### CPU Limit

```typescript
// Skip parsing large emails
if (message.rawSize > 5_000_000) {
  await message.forward('inbox@example.com');
  return;
}
```

Monitor: `npx wrangler tail`

