## Persistent Data with Bucket Mounting

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const sandbox = getSandbox(env.Sandbox, 'data-processor');
    
    // Mount R2 bucket (production only)
    await sandbox.mountBucket(env.DATA_BUCKET, '/data', {
      readOnly: false
    });
    
    // Process files in bucket
    const result = await sandbox.exec('python3 /workspace/process.py', {
      env: { DATA_DIR: '/data/input' }
    });
    
    // Results written to /data/output are persisted in R2
    return Response.json({ success: result.success });
  }
};
```

