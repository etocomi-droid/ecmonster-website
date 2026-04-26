## Python Handler

```python
from workers import WorkerEntrypoint

class Default(WorkerEntrypoint):
    async def scheduled(self, controller, env, ctx):
        data = await env.MY_KV.get("key")
        ctx.waitUntil(env.DB.execute("DELETE FROM logs WHERE created_at < datetime('now', '-7 days')"))
```

