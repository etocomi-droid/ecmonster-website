## Framework Patterns

### React

```tsx
import { useState } from 'react';
import Turnstile from '@marsidev/react-turnstile';

export default function Form() {
  const [token, setToken] = useState<string | null>(null);

  return (
    <form onSubmit={async (e) => {
      e.preventDefault();
      if (!token) return;
      await fetch('/api/submit', { 
        method: 'POST',
        body: JSON.stringify({ 'cf-turnstile-response': token })
      });
    }}>
      <Turnstile siteKey="YOUR_SITE_KEY" onSuccess={setToken} />
      <button disabled={!token}>Submit</button>
    </form>
  );
}
```

### Vue / Svelte

```vue
<!-- Vue: npm install vue-turnstile -->
<VueTurnstile :site-key="SITE_KEY" @success="token = $event" />

<!-- Svelte: npm install svelte-turnstile -->
<Turnstile siteKey={SITE_KEY} on:turnstile-callback={(e) => token = e.detail.token} />
```

