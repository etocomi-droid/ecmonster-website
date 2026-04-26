## Sessions (Isolated Contexts)

Each session maintains own shell state, env vars, cwd, process namespace.

```typescript
// Create with context
const session = await sandbox.createSession({
  id: 'user-123',
  cwd: '/workspace/user123',
  env: { USER_ID: '123' }
});

// Use (full sandbox API)
await session.exec('echo $USER_ID');
await session.writeFile('config.txt', 'data');

// Manage
await sandbox.getSession('user-123');
await sandbox.deleteSession('user-123');
```

