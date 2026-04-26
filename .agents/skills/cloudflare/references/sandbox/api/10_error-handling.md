## Error Handling

```typescript
// Command errors
const result = await sandbox.exec('python3 invalid.py');
if (!result.success) {
  console.error('Exit code:', result.exitCode);
  console.error('Stderr:', result.stderr);
}

// SDK errors
try {
  await sandbox.readFile('/nonexistent');
} catch (error) {
  if (error.code === 'FILE_NOT_FOUND') { /* ... */ }
  else if (error.code === 'CONTAINER_NOT_READY') { /* retry */ }
  else if (error.code === 'TIMEOUT') { /* ... */ }
}

// Retry pattern (see gotchas.md for full implementation)
```


