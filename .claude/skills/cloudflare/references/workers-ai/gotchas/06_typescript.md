## TypeScript

```typescript
interface Env {
  AI: Ai; // From @cloudflare/workers-types
}

interface TextGenerationResponse { response: string; }
interface EmbeddingResponse { data: number[][]; shape: number[]; }
```

