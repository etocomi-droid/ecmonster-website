## Testing Transactions

```typescript
it("rolls back on error", async () => {
  const id = env.BANK.idFromName("transaction-test");
  
  await runInDurableObject(env.BANK, id, async (instance, state) => {
    await state.storage.put("balance", 100);
    
    await expect(
      state.storage.transaction(async () => {
        await state.storage.put("balance", 50);
        throw new Error("Cancel");
      })
    ).rejects.toThrow("Cancel");
    
    const balance = await state.storage.get("balance");
    expect(balance).toBe(100); // Rolled back
  });
});
```
