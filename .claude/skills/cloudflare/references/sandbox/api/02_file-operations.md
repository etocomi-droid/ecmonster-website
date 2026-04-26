## File Operations

```typescript
// Read/Write
const { content } = await sandbox.readFile('/workspace/data.txt');
await sandbox.writeFile('/workspace/file.txt', 'content');  // Auto-creates dirs

// List/Delete
const files = await sandbox.listFiles('/workspace');
await sandbox.deleteFile('/workspace/temp.txt');
await sandbox.deleteFile('/workspace/dir', { recursive: true });

// Utils
await sandbox.mkdir('/workspace/dir', { recursive: true });
await sandbox.pathExists('/workspace/file.txt');
```

