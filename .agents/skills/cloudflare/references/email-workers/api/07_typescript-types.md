## TypeScript Types

```typescript
import { 
  ForwardableEmailMessage,
  EmailMessage 
} from 'cloudflare:email';

interface Env {
  EMAIL: SendEmail;
  EMAIL_ARCHIVE: KVNamespace;
  ALLOWED_SENDERS: KVNamespace;
}

export default {
  async email(
    message: ForwardableEmailMessage,
    env: Env,
    ctx: ExecutionContext
  ): Promise<void> {
    // Fully typed
  }
};
```
