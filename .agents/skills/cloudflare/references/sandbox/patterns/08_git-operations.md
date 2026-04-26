## Git Operations

```typescript
// Clone repo
await sandbox.exec('git clone https://github.com/user/repo.git /workspace/repo');

// Authenticated (use env secrets)
await sandbox.exec(`git clone https://${env.GITHUB_TOKEN}@github.com/user/repo.git`);
```
