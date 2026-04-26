## Quick Start

1. Navigate to domain > Zaraz in Cloudflare dashboard
2. Click "Start setup"
3. Add tools (Google Analytics, Facebook Pixel, etc.)
4. Configure triggers (when tools fire)
5. Add tracking code to your site:

```javascript
// Track page view
zaraz.track('page_view');

// Track custom event
zaraz.track('button_click', { button_id: 'cta' });

// Set user properties
zaraz.set('userId', 'user_123');
```

