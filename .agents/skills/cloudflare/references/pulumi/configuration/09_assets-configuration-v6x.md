## Assets Configuration (v6.x)

Serve static assets from Workers:

```typescript
const worker = new cloudflare.WorkerScript("app", {
    accountId: accountId,
    name: "my-app",
    content: code,
    assets: {
        path: "./public", // Local directory
        // Assets uploaded and served from Workers
    },
});
```

