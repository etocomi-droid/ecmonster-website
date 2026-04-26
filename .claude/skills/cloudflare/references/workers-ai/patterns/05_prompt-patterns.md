## Prompt Patterns

```typescript
// System prompts
const PROMPTS = {
  json: 'Respond with valid JSON only.',
  concise: 'Keep responses brief.',
  cot: 'Think step by step before answering.'
};

// Few-shot
messages: [
  { role: 'system', content: 'Extract as JSON' },
  { role: 'user', content: 'John bought 3 apples for $5' },
  { role: 'assistant', content: '{"name":"John","item":"apples","qty":3}' },
  { role: 'user', content: actualInput }
]
```

