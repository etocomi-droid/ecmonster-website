## Local Development Confusion

**Issue:** Smart Placement doesn't work in `wrangler dev`.

**Explanation:** Smart Placement only activates in production deployments, not local development.

**Solution:** Test Smart Placement in staging environment: `wrangler deploy --env staging`

