## TypeScript Types

```typescript
interface Env {
  EMAIL: SendEmail;
  ARCHIVE: KVNamespace;
  ATTACHMENTS: R2Bucket;
  WEBHOOK_URL: string;
}

export default {
  async email(message: ForwardableEmailMessage, env: Env, ctx: ExecutionContext) {}
};
```

