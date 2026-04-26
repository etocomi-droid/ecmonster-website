## Testing

### Environment-Based Keys

```javascript
const SITE_KEY = process.env.NODE_ENV === 'production'
  ? 'YOUR_PRODUCTION_SITE_KEY'
  : '1x00000000000000000000AA'; // Always passes

const SECRET_KEY = process.env.NODE_ENV === 'production'
  ? process.env.TURNSTILE_SECRET
  : '1x0000000000000000000000000000000AA';
```
