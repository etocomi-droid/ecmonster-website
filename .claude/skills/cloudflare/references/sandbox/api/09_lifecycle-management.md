## Lifecycle Management

```typescript
// Terminate container immediately
await sandbox.destroy();

// REQUIRED when using keepAlive: true
const sandbox = getSandbox(env.Sandbox, 'temp', { keepAlive: true });
try {
  await sandbox.writeFile('/tmp/code.py', code);
  const result = await sandbox.exec('python /tmp/code.py');
  return result.stdout;
} finally {
  await sandbox.destroy();  // Free resources
}
```

Deletes: files, processes, sessions, network connections, exposed ports.

