## Deployment Workflow

### Development
1. Write snippet code locally
2. Test syntax with `node snippet.js` or TypeScript compiler
3. Deploy to Dashboard or use API with `Save as Draft`
4. Test with Preview/HTTP tabs in Dashboard
5. Enable rule when ready

### Production
1. Store snippet code in version control
2. Use Terraform/Pulumi for reproducible deployments
3. Deploy to staging zone first
4. Test with real traffic (use low-traffic subdomain)
5. Apply to production zone
6. Monitor with Analytics/Logpush

