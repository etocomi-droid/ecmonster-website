## Widget Configuration

### Complete Options Object

```javascript
{
  // Required
  sitekey: 'YOUR_SITE_KEY',        // Widget sitekey from dashboard

  // Callbacks
  callback: (token) => {},          // Success - token ready
  'error-callback': (code) => {},   // Error occurred
  'expired-callback': () => {},     // Token expired (>5min)
  'timeout-callback': () => {},     // Challenge timeout
  'before-interactive-callback': () => {}, // Before showing checkbox
  'after-interactive-callback': () => {},  // After user interacts
  'unsupported-callback': () => {}, // Browser doesn't support Turnstile

  // Appearance
  theme: 'auto',                    // 'light' | 'dark' | 'auto'
  size: 'normal',                   // 'normal' | 'compact' | 'flexible'
  tabindex: 0,                      // Tab order (accessibility)
  language: 'auto',                 // ISO 639-1 code or 'auto'

  // Behavior
  execution: 'render',              // 'render' (auto) | 'execute' (manual)
  appearance: 'always',             // 'always' | 'execute' | 'interaction-only'
  retry: 'auto',                    // 'auto' | 'never'
  'retry-interval': 8000,           // Retry interval (ms), default 8000
  'refresh-expired': 'auto',        // 'auto' | 'manual' | 'never'

  // Form Integration
  'response-field': true,           // Add hidden input (default: true)
  'response-field-name': 'cf-turnstile-response', // Hidden input name

  // Analytics & Data
  action: 'login',                  // Action name (for analytics)
  cData: 'user-session-123',        // Custom data (returned in siteverify)
}
```

### Key Options Explained

**`execution`:**
- `'render'` (default): Challenge starts immediately on render
- `'execute'`: Wait for `turnstile.execute()` call

**`appearance`:**
- `'always'` (default): Widget always visible
- `'execute'`: Hidden until `execute()` called
- `'interaction-only'`: Hidden until user interaction needed

**`refresh-expired`:**
- `'auto'` (default): Auto-refresh expired tokens
- `'manual'`: App must call `reset()` after expiry
- `'never'`: No refresh, expired-callback triggered

**`retry`:**
- `'auto'` (default): Auto-retry failed challenges
- `'never'`: Don't retry, trigger error-callback

