## Testing SQL Storage

```typescript
it("creates and queries users", async () => {
  const id = env.USER_MANAGER.idFromName("test");
  await runInDurableObject(env.USER_MANAGER, id, async (instance, state) => {
    await instance.createUser("alice@example.com", "Alice");
    const user = await instance.getUser("alice@example.com");
    expect(user).toEqual({ email: "alice@example.com", name: "Alice" });
  });
});

it("handles schema migrations", async () => {
  const id = env.USER_MANAGER.idFromName("migration-test");
  await runInDurableObject(env.USER_MANAGER, id, async (instance, state) => {
    const version = state.storage.sql.exec(
      "SELECT value FROM _meta WHERE key = 'schema_version'"
    ).one()?.value;
    expect(version).toBe("1");
  });
});
```

