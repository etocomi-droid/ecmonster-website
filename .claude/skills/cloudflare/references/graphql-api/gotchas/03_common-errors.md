## Common Errors

### "Access denied" / "authentication error"

**Cause:** Token lacks required permission or wrong scope.

**Solution:** Account-scoped queries need **Account Analytics: Read**. Zone-scoped queries need **Zone Analytics: Read**. Verify: `curl -s https://api.cloudflare.com/client/v4/user/tokens/verify -H "Authorization: Bearer $TOKEN"`

### "field not found" / "Cannot query field"

**Cause:** Wrong dataset name, nonexistent field, or wrong scope (zone vs. account).

**Solution:** Names are case-sensitive camelCase (`httpRequestsAdaptiveGroups`). Zone datasets go under `zones(...)`, account datasets under `accounts(...)`. Use introspection to verify.

### "filter is required" / empty results

**Cause:** Missing required time range filter or incorrect zone/account tag.

**Solution:** Always include `datetime_gt` / `datetime_lt` (or `_geq` / `_leq`).

### "limit is required" / "limit exceeds maximum"

**Cause:** Missing `limit` or exceeding node's max page size.

**Solution:** Always specify `limit`. Max varies by dataset (typically 10,000 for groups, 100 for raw events). Check via settings query.

### "query is too complex" / "query exceeds budget"

**Cause:** Too many fields, datasets, or too broad a time range.

**Solution:** Reduce time range, request fewer dimensions/metrics, break into smaller queries. Monitor `cost` and `budget` in responses.

### 200 Response with Errors

GraphQL returns HTTP 200 even on failures. **Always check `response.errors`:**

```json
{ "data": null, "errors": [{ "message": "filter is required for httpRequestsAdaptiveGroups" }] }
```

