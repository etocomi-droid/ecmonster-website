## Theming & Design Tokens

```typescript
import type { UIConfig } from '@cloudflare/realtimekit';

const uiConfig: UIConfig = {
  designTokens: {
    colors: {
      brand: { 500: '#0066ff', 600: '#0052cc' },
      background: { 1000: '#1A1A1A', 900: '#2D2D2D' },
      text: { 1000: '#FFFFFF', 900: '#E0E0E0' }
    },
    borderRadius: 'extra-rounded',  // 'rounded' | 'extra-rounded' | 'sharp'
    theme: 'dark'  // 'light' | 'dark'
  },
  logo: { url: 'https://example.com/logo.png', altText: 'Company' }
};

// Apply to React
<RtkMeeting authToken={token} config={uiConfig} onLeave={() => {}} />

// Or use CSS variables
// :root { --rtk-color-brand-500: #0066ff; --rtk-border-radius: 12px; }
```

