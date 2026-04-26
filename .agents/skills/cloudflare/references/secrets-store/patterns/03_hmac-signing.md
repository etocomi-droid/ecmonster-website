## HMAC Signing

```typescript
interface Env {
  HMAC_SECRET: { get(): Promise<string> };
}

async function signRequest(data: string, secret: string): Promise<string> {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]
  );
  const sig = await crypto.subtle.sign("HMAC", key, enc.encode(data));
  return btoa(String.fromCharCode(...new Uint8Array(sig)));
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const secret = await env.HMAC_SECRET.get();
    const payload = await request.text();
    const signature = await signRequest(payload, secret);
    return Response.json({ signature });
  }
}
```

