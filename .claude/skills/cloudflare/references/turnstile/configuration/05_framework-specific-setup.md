## Framework-Specific Setup

### React
```bash
npm install @marsidev/react-turnstile
```
```jsx
import Turnstile from '@marsidev/react-turnstile';

<Turnstile
  siteKey="YOUR_SITE_KEY"
  onSuccess={(token) => console.log(token)}
/>
```

### Vue
```bash
npm install vue-turnstile
```
```vue
<template>
  <VueTurnstile site-key="YOUR_SITE_KEY" @success="onSuccess" />
</template>
<script setup>
import VueTurnstile from 'vue-turnstile';
</script>
```

### Svelte
```bash
npm install svelte-turnstile
```
```svelte
<script>
import Turnstile from 'svelte-turnstile';
</script>
<Turnstile siteKey="YOUR_SITE_KEY" on:turnstile-callback={handleToken} />
```

### Next.js (App Router)
```tsx
// app/components/TurnstileWidget.tsx
'use client';
import { useEffect, useRef } from 'react';

export default function TurnstileWidget({ sitekey, onSuccess }) {
  const ref = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    if (ref.current && window.turnstile) {
      const widgetId = window.turnstile.render(ref.current, {
        sitekey,
        callback: onSuccess
      });
      return () => window.turnstile.remove(widgetId);
    }
  }, [sitekey, onSuccess]);
  
  return <div ref={ref} />;
}
```

