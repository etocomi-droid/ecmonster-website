## Use Case Implementations

### AI Code Execution
```typescript
async function deployGeneratedCode(name: string, code: string) {
  const file = new File([code], `${name}.mjs`, { type: "application/javascript+module" });
  await client.workersForPlatforms.dispatch.namespaces.scripts.update("production", name, {
    account_id: accountId,
    metadata: { main_module: `${name}.mjs`, tags: [name, "ai-generated"] },
    files: [file],
  });
}

// Short limits for untrusted code
const userWorker = env.DISPATCHER.get(sessionId, {}, { limits: { cpuMs: 5, subRequests: 3 } });
```

**VibeSDK:** For AI-powered code generation + deployment platforms, see [VibeSDK](https://github.com/cloudflare/vibesdk) - handles AI generation, sandbox execution, live preview, and deployment.

Reference: [AI Vibe Coding Platform Architecture](https://developers.cloudflare.com/reference-architecture/diagrams/ai/ai-vibe-coding-platform/)

### Edge Functions Platform
```typescript
// Route: /customer-id/function-name
const [customerId, functionName] = new URL(request.url).pathname.split("/").filter(Boolean);
const workerName = `${customerId}-${functionName}`;
const userWorker = env.DISPATCHER.get(workerName);
```

### Website Builder
- Deploy static assets + Worker code
- See [api.md](./api.md#static-assets) for full implementation
- Salt hashes for asset isolation

