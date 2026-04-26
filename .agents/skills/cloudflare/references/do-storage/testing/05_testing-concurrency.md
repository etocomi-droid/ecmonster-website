## Testing Concurrency

```typescript
it("handles concurrent increments safely", async () => {
  const id = env.COUNTER.idFromName("concurrent-test");
  
  // Parallel increments
  const results = await Promise.all([
    runInDurableObject(env.COUNTER, id, (i) => i.increment()),
    runInDurableObject(env.COUNTER, id, (i) => i.increment()),
    runInDurableObject(env.COUNTER, id, (i) => i.increment())
  ]);
  
  // All should get unique values
  expect(new Set(results).size).toBe(3);
  expect(Math.max(...results)).toBe(3);
});
```

