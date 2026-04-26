## Command Execution

```typescript
// Basic
const result = await sandbox.exec('python3 script.py');
// Returns: { stdout, stderr, exitCode, success, duration }

// With options
await sandbox.exec('python3 test.py', {
  cwd: '/workspace/project',
  env: { API_KEY: 'secret' },
  stream: true,
  onOutput: (stream, data) => console.log(data)
});
```

