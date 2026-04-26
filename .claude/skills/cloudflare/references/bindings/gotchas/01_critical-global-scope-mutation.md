## Critical: Global Scope Mutation

### ❌ THE #1 GOTCHA: Caching env in Global Scope

```typescript
// ❌ DANGEROUS - env cached at deploy time
const apiKey = env.API_KEY;  // ERROR: env not available in global scope

export default {
  async fetch(request: Request, env: Env) {
    // Uses undefined or stale value!
  }
}
```

**Why it breaks:**
- `env` not available in global scope
- If using workarounds, secrets may not update without redeployment
- Leads to "Cannot read property 'X' of undefined" errors

**✅ Always access env per-request:**
```typescript
export default {
  async fetch(request: Request, env: Env) {
    const apiKey = env.API_KEY;  // Fresh every request
  }
}
```

