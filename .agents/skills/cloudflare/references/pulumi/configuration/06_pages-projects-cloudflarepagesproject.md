## Pages Projects (cloudflare.PagesProject)

```typescript
const pages = new cloudflare.PagesProject("my-site", {
    accountId, name: "my-site", productionBranch: "main",
    buildConfig: {buildCommand: "npm run build", destinationDir: "dist"},
    source: {
        type: "github",
        config: {owner: "my-org", repoName: "my-repo", productionBranch: "main"},
    },
    deploymentConfigs: {
        production: {
            environmentVariables: {NODE_VERSION: "18"},
            kvNamespaces: {MY_KV: kv.id},
            d1Databases: {DB: db.id},
        },
    },
});
```

