## SendEmail Interface

```typescript
interface SendEmail {
  send(message: EmailMessage): Promise<void>;
}

// Usage
await env.EMAIL.send(new EmailMessage(from, to, mimeContent));
```

