## Server Validation

### Cloudflare Workers

```typescript
interface Env {
  TURNSTILE_SECRET: string;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }
    
    const formData = await request.formData();
    const token = formData.get('cf-turnstile-response');
    
    if (!token) {
      return new Response('Missing token', { status: 400 });
    }
    
    // Validate token
    const ip = request.headers.get('CF-Connecting-IP');
    const result = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        secret: env.TURNSTILE_SECRET,
        response: token,
        remoteip: ip
      })
    });
    
    const validation = await result.json();
    
    if (!validation.success) {
      return new Response('CAPTCHA validation failed', { status: 403 });
    }
    
    // Process form...
    return new Response('Success');
  }
};
```

### Pages Functions

```typescript
// functions/submit.ts - same pattern as Workers, use ctx.env and ctx.request
export const onRequestPost: PagesFunction<{ TURNSTILE_SECRET: string }> = async (ctx) => {
  const token = (await ctx.request.formData()).get('cf-turnstile-response');
  // Validate with ctx.env.TURNSTILE_SECRET (same as Workers pattern above)
};
```

