## Cloudflare Pages Plugin

```bash
npm install @cloudflare/pages-plugin-turnstile
```

```typescript
// functions/_middleware.ts
import turnstilePlugin from '@cloudflare/pages-plugin-turnstile';

export const onRequest = turnstilePlugin({
  secret: 'YOUR_SECRET_KEY',
  onError: () => new Response('CAPTCHA failed', { status: 403 })
});
```