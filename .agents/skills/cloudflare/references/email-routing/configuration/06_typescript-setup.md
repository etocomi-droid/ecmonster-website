## TypeScript Setup

```bash
npm install --save-dev @cloudflare/workers-types
```

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ES2022",
    "lib": ["ES2022"],
    "types": ["@cloudflare/workers-types"],
    "moduleResolution": "bundler",
    "strict": true
  }
}
```

```typescript
import type { ForwardableEmailMessage } from "@cloudflare/workers-types";

export default {
  async email(message: ForwardableEmailMessage, env: Env, ctx: ExecutionContext): Promise<void> {
    await message.forward("dest@example.com");
  }
} satisfies ExportedHandler<Env>;
```

