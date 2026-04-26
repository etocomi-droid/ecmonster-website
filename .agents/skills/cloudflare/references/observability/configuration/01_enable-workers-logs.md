### Enable Workers Logs

```jsonc
{
  "observability": {
    "enabled": true,
    "head_sampling_rate": 1  // 100% sampling (default)
  }
}
```

**Best Practice**: Use structured JSON logging for better indexing

```typescript
// Good - structured logging
console.log({ 
  user_id: 123, 
  action: "login", 
  status: "success",
  duration_ms: 45
});

// Avoid - unstructured string
console.log("user_id: 123 logged in successfully in 45ms");
```

