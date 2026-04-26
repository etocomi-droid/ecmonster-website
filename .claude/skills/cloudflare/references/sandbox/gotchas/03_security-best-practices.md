## Security Best Practices

### Sandbox Isolation
- Each sandbox = isolated container (filesystem, network, processes)
- Use unique sandbox IDs per tenant for multi-tenant apps
- Sandboxes cannot communicate directly

### Input Validation

```typescript
// ❌ DANGEROUS: Command injection
const result = await sandbox.exec(`python3 -c "${userCode}"`);

// ✅ SAFE: Write to file, execute file
await sandbox.writeFile('/workspace/user_code.py', userCode);
const result = await sandbox.exec('python3 /workspace/user_code.py');
```

### Resource Limits

```typescript
// Timeout long-running commands
const result = await sandbox.exec('python3 script.py', {
  timeout: 30000  // 30 seconds
});
```

### Secrets Management

```typescript
// ❌ NEVER hardcode secrets
const token = 'ghp_abc123';

// ✅ Use environment secrets
const token = env.GITHUB_TOKEN;

// Pass to sandbox via exec env
const result = await sandbox.exec('git clone ...', {
  env: { GIT_TOKEN: token }
});
```

### Preview URL Security
Preview URLs include auto-generated tokens:
```
https://8080-sandbox-abc123def456.yourdomain.com
```
Token changes on each expose operation, preventing unauthorized access.

