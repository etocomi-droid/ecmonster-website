## Webhook Handler

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const signature = request.headers.get('Webhook-Signature');
    const body = await request.text();
    if (!signature || !await verifyWebhook(signature, body, env.WEBHOOK_SECRET)) {
      return new Response('Unauthorized', { status: 401 });
    }
    const payload = JSON.parse(body);
    if (payload.readyToStream) console.log(`Video ${payload.uid} ready`);
    return new Response('OK');
  }
};

async function verifyWebhook(sig: string, body: string, secret: string): Promise<boolean> {
  const parts = Object.fromEntries(sig.split(',').map(p => p.split('=')));
  const timestamp = parseInt(parts.time || '0', 10);
  if (Math.abs(Date.now() / 1000 - timestamp) > 300) return false;
  
  const key = await crypto.subtle.importKey(
    'raw', new TextEncoder().encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']
  );
  const computed = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(`${timestamp}.${body}`));
  const hex = Array.from(new Uint8Array(computed), b => b.toString(16).padStart(2, '0')).join('');
  return hex === parts.sig1;
}
```

