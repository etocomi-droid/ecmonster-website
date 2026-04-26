## Cron Triggers (Pre-warming)

```jsonc
{
  "triggers": {
    "crons": ["*/5 * * * *"]  // Every 5 minutes
  }
}
```

```typescript
export default {
  async scheduled(event: ScheduledEvent, env: Env) {
    const sandbox = getSandbox(env.Sandbox, 'main');
    await sandbox.exec('echo "keepalive"');  // Wake sandbox
  }
};
```

