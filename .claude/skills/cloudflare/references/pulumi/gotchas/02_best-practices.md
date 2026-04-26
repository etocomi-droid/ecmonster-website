## Best Practices

1. **Always set compatibilityDate** - Locks Worker behavior, prevents breaking changes
2. **Build before deploy** - Pulumi doesn't bundle; use Command resource or CI build step
3. **Match binding names** - Case-sensitive, must match between Pulumi and Worker code
4. **Use dependsOn for migrations** - Ensure D1 migrations run before Worker deploys
5. **Version Worker content** - Add VERSION binding to force redeployment on content changes
6. **Store secrets in stack config** - Use `pulumi config set --secret` for API keys

