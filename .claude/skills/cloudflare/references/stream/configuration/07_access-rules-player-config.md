## Access Rules & Player Config

```typescript
// Access rules: allow US/CA, block CN/RU, or IP allowlist
const geoRestrict = [
  { type: 'ip.geoip.country', action: 'allow', country: ['US', 'CA'] },
  { type: 'any', action: 'block' }
];

// Player params for iframe
const playerParams = new URLSearchParams({
  autoplay: 'true', muted: 'true', preload: 'auto', defaultTextTrack: 'en'
});
```

