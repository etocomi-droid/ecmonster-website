## Error Handling

The TypeScript SDK provides typed error classes for robust error handling:

```typescript
import Cloudflare from 'cloudflare';
import { APIError, APIConnectionError, RateLimitError } from 'cloudflare';

async function enableArgoWithErrorHandling(client: Cloudflare, zoneId: string) {
  try {
    const result = await client.argo.smartRouting.edit({
      zone_id: zoneId,
      value: 'on',
    });
    return result;
  } catch (error) {
    if (error instanceof RateLimitError) {
      console.error('Rate limited. Retry after:', error.response?.headers.get('retry-after'));
      // Implement exponential backoff
    } else if (error instanceof APIError) {
      console.error('API error:', error.status, error.message);
      if (error.status === 403) {
        console.error('Permission denied - check API token scopes');
      } else if (error.status === 400) {
        console.error('Bad request - verify zone_id and payload');
      }
    } else if (error instanceof APIConnectionError) {
      console.error('Connection failed:', error.message);
      // Retry with exponential backoff
    } else {
      console.error('Unexpected error:', error);
    }
    throw error;
  }
}
```

**Python Error Handling:**
```python
from cloudflare import Cloudflare, APIError, RateLimitError

def enable_argo_with_error_handling(client: Cloudflare, zone_id: str):
    try:
        result = client.argo.smart_routing.edit(zone_id=zone_id, value='on')
        return result
    except RateLimitError as e:
        print(f"Rate limited. Retry after: {e.response.headers.get('retry-after')}")
        raise
    except APIError as e:
        print(f"API error: {e.status} - {e.message}")
        if e.status == 403:
            print('Permission denied - check API token scopes')
        elif e.status == 400:
            print('Bad request - verify zone_id and payload')
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
```

