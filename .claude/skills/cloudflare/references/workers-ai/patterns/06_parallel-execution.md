## Parallel Execution

```typescript
const [sentiment, summary, embedding] = await Promise.all([
  env.AI.run('@cf/mistral/mistral-7b-instruct-v0.1', { messages: sentimentPrompt }),
  env.AI.run('@cf/meta/llama-3.1-8b-instruct', { messages: summaryPrompt }),
  env.AI.run('@cf/baai/bge-base-en-v1.5', { text })
]);
```

