## Framework Gotchas

### React: Widget Re-mounting
**Problem:** Widget re-renders on state change, losing token.

**Solution:** Control lifecycle with useRef.
```tsx
function TurnstileWidget({ onToken }) {
  const containerRef = useRef(null);
  const widgetIdRef = useRef(null);
  
  useEffect(() => {
    if (containerRef.current && !widgetIdRef.current) {
      widgetIdRef.current = window.turnstile.render(containerRef.current, {
        sitekey: 'YOUR_SITE_KEY',
        callback: onToken
      });
    }
    return () => {
      if (widgetIdRef.current) {
        window.turnstile.remove(widgetIdRef.current);
        widgetIdRef.current = null;
      }
    };
  }, []);
  
  return <div ref={containerRef} />;
}
```

### React StrictMode: Double Render
**Problem:** Widget renders twice in dev due to StrictMode.

**Solution:** Use cleanup function.
```tsx
useEffect(() => {
  const widgetId = window.turnstile.render('#container', { sitekey });
  return () => window.turnstile.remove(widgetId);
}, []);
```

### Next.js: SSR Hydration
**Problem:** `window.turnstile` undefined during SSR.

**Solution:** Use `'use client'` or dynamic import with `ssr: false`.
```tsx
'use client';
export default function Turnstile() { /* component */ }
```

### SPA: Navigation Without Cleanup
**Problem:** Navigating leaves orphaned widgets.

**Solution:** Remove widget in cleanup.
```javascript
// Vue
onBeforeUnmount(() => window.turnstile.remove(widgetId));

// React
useEffect(() => () => window.turnstile.remove(widgetId), []);
```

