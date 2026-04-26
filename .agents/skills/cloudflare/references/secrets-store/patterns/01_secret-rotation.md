## Secret Rotation

Zero-downtime rotation with versioned naming (`api_key_v1`, `api_key_v2`):

```typescript
interface Env {
  PRIMARY_KEY: { get(): Promise<string> };
  FALLBACK_KEY?: { get(): Promise<string> };
}

async function fetchWithAuth(url: string, key: string) {
  return fetch(url, { headers: { "Authorization": `Bearer ${key}` } });
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    let resp = await fetchWithAuth("https://api.example.com", await env.PRIMARY_KEY.get());
    
    // Fallback during rotation
    if (!resp.ok && env.FALLBACK_KEY) {
      resp = await fetchWithAuth("https://api.example.com", await env.FALLBACK_KEY.get());
    }
    
    return resp;
  }
}
```

Workflow: Create `api_key_v2` → add fallback binding → deploy → swap primary → deploy → remove `v1`

