## Common Errors

### "Argo unavailable"

**Problem:** API returns error "Argo Smart Routing is unavailable for this zone"

**Cause:** Zone not eligible or billing not set up

**Solution:**
1. Verify zone has Enterprise or higher plan
2. Check billing is configured in Account → Billing
3. Ensure payment method is valid and current
4. Contact Cloudflare support if eligibility unclear

### "Cannot enable/disable"

**Problem:** API call succeeds but status remains unchanged, or `editable: false` in GET response

**Cause:** Insufficient permissions or zone restrictions

**Solution:**
1. Check API token has `Zone:Argo Smart Routing:Edit` permission
2. Verify `editable: true` in GET response before attempting PATCH
3. If `editable: false`, check:
   - Billing configured for account
   - Zone plan includes Argo (Enterprise+)
   - No active zone holds or suspensions
   - API token has correct scopes

### `editable: false` Error

**Problem:** GET request returns `"editable": false`, preventing enable/disable

**Cause:** Zone-level restrictions from billing, plan, or permissions

**Solution Pattern:**
```typescript
const status = await client.argo.smartRouting.get({ zone_id: zoneId });

if (!status.editable) {
  // Don't attempt to modify - will fail
  console.error('Cannot modify Argo settings:');
  console.error('- Check billing is configured');
  console.error('- Verify zone has Enterprise+ plan');
  console.error('- Confirm API token has Edit permission');
  throw new Error('Argo is not editable for this zone');
}

// Safe to proceed with enable/disable
await client.argo.smartRouting.edit({ zone_id: zoneId, value: 'on' });
```

### Rate Limiting

**Problem:** `429 Too Many Requests` error from API

**Cause:** Exceeded API rate limits (typically 1200 requests per 5 minutes)

**Solution:**
```typescript
import { RateLimitError } from 'cloudflare';

try {
  await client.argo.smartRouting.edit({ zone_id: zoneId, value: 'on' });
} catch (error) {
  if (error instanceof RateLimitError) {
    const retryAfter = error.response?.headers.get('retry-after');
    console.log(`Rate limited. Retry after ${retryAfter} seconds`);
    
    // Implement exponential backoff
    await new Promise(resolve => setTimeout(resolve, (retryAfter || 60) * 1000));
    // Retry request
  }
}
```

