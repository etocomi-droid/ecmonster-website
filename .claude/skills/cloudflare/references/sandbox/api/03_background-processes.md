## Background Processes

```typescript
// Start
const process = await sandbox.startProcess('python3 -m http.server 8080', {
  processId: 'web-server',
  cwd: '/workspace/public',
  env: { PORT: '8080' }
});
// Returns: { id, pid, command }

// Wait for readiness
await process.waitForPort(8080);  // Wait for port to listen
await process.waitForLog(/Server running/);  // Wait for log pattern
await process.waitForExit();  // Wait for completion

// Management
const processes = await sandbox.listProcesses();
const info = await sandbox.getProcess('web-server');
await sandbox.stopProcess('web-server');
const logs = await sandbox.getProcessLogs('web-server');
```

