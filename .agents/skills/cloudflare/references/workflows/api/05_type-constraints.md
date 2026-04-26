## Type Constraints

Params and step returns must be `Rpc.Serializable<T>`:

```typescript
// ✅ Valid types
type ValidParams = {
  userId: string;
  count: number;
  tags: string[];
  metadata: Record<string, unknown>;
};

// ❌ Invalid types
type InvalidParams = {
  callback: () => void;      // Functions not serializable
  symbol: symbol;            // Symbols not serializable
  circular: any;             // Circular references not allowed
};

// Step returns follow same rules
const result = await step.do('fetch', async () => {
  return { userId: '123', data: [1, 2, 3] }; // ✅ Plain object
});
```

