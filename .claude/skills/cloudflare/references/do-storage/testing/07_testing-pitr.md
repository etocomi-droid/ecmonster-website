## Testing PITR

```typescript
it("restores from bookmark", async () => {
  const id = env.MY_DO.idFromName("pitr-test");
  
  // Create checkpoint
  const bookmark = await runInDurableObject(env.MY_DO, id, async (instance, state) => {
    await state.storage.put("value", 1);
    return await state.storage.getCurrentBookmark();
  });
  
  // Modify and restore
  await runInDurableObject(env.MY_DO, id, async (instance, state) => {
    await state.storage.put("value", 2);
    await state.storage.onNextSessionRestoreBookmark(bookmark);
    state.abort();
  });
  
  // Verify restored
  await runInDurableObject(env.MY_DO, id, async (instance, state) => {
    const value = await state.storage.get("value");
    expect(value).toBe(1);
  });
});
```

