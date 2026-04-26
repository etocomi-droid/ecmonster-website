### "wrangler.toml not consumed" - Config drift

**Problem:** Local wrangler dev works, Pulumi deploy fails  
**Cause:** Pulumi ignores wrangler.toml - must duplicate config  
**Solution:** Generate wrangler.toml from Pulumi or keep synced manually

```typescript
// Pattern: Export Pulumi config to wrangler.toml
const workerConfig = {
    name: "my-worker",
    compatibilityDate: "2025-01-01",
    compatibilityFlags: ["nodejs_compat"],
};

new command.local.Command("generate-wrangler", {
    create: pulumi.interpolate`cat > wrangler.toml <<EOF
name = "${workerConfig.name}"
compatibility_date = "${workerConfig.compatibilityDate}"
compatibility_flags = ${JSON.stringify(workerConfig.compatibilityFlags)}
EOF`,
});
```

