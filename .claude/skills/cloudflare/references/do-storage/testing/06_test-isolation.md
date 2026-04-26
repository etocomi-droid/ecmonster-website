## Test Isolation

```typescript
// Per-test unique IDs
let testId: string;
beforeEach(() => { testId = crypto.randomUUID(); });

it("isolated test", async () => {
  const id = env.MY_DO.idFromName(testId);
  // Uses unique DO instance
});

// Cleanup pattern
it("with cleanup", async () => {
  const id = env.MY_DO.idFromName("cleanup-test");
  try {
    await runInDurableObject(env.MY_DO, id, async (instance) => {});
  } finally {
    await runInDurableObject(env.MY_DO, id, async (instance, state) => {
      await state.storage.deleteAll();
    });
  }
});
```

