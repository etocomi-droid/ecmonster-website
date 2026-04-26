## Testing Alarms

```typescript
import { runDurableObjectAlarm } from "cloudflare:test";

it("processes batch on alarm", async () => {
  const id = env.BATCH_PROCESSOR.idFromName("test");
  
  // Add items
  await runInDurableObject(env.BATCH_PROCESSOR, id, async (instance) => {
    await instance.addItem("item1");
    await instance.addItem("item2");
  });
  
  // Trigger alarm
  await runDurableObjectAlarm(env.BATCH_PROCESSOR, id);
  
  // Verify processed
  await runInDurableObject(env.BATCH_PROCESSOR, id, async (instance, state) => {
    const count = state.storage.sql.exec(
      "SELECT COUNT(*) as count FROM processed_items"
    ).one().count;
    expect(count).toBe(2);
  });
});
```

