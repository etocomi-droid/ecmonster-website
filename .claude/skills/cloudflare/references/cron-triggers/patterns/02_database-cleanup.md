## Database Cleanup

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const result = await env.DB.prepare(`DELETE FROM sessions WHERE expires_at < datetime('now')`).run();
    console.log(`Deleted ${result.meta.changes} expired sessions`);
    ctx.waitUntil(env.DB.prepare("VACUUM").run());
  },
};
```

