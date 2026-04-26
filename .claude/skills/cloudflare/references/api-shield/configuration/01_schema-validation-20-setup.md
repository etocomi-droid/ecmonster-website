## Schema Validation 2.0 Setup

> ⚠️ **Classic Schema Validation deprecated.** Use Schema Validation 2.0.

**Upload schema (Dashboard):**
```
Security > API Shield > Schema Validation > Add validation
- Upload .yml/.yaml/.json (OpenAPI v3.0)
- Endpoints auto-added to Endpoint Management
- Action: Log | Block | None
- Body inspection: JSON payloads
```

**Change validation action:**
```
Security > API Shield > Settings > Schema Validation
Per-endpoint: Filter → ellipses → Change action
Default action: Set global mitigation action
```

**Migration from Classic:**
```
1. Export existing schema (if available)
2. Delete all Classic schema validation rules
3. Wait 5 min for cache clear
4. Re-upload via Schema Validation 2.0 interface
5. Verify in Security > Events
```

**Fallthrough rule** (catch-all unknown endpoints):
```
Security > API Shield > Settings > Fallthrough > Use Template
- Select hostnames
- Create rule with cf.api_gateway.fallthrough_triggered
- Action: Log (discover) or Block (strict)
```

**Body inspection:** Supports `application/json`, `*/*`, `application/*`. Disable origin MIME sniffing to prevent bypasses.

