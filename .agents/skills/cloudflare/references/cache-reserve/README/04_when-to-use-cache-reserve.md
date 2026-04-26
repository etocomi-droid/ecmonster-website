## When to Use Cache Reserve

```
Need persistent caching?
├─ High origin egress costs → Cache Reserve ✓
├─ Long-tail content (archives, media libraries) → Cache Reserve ✓
├─ Already using Smart Shield Advanced → Included! ✓
├─ Video streaming with seeking (range requests) → ✗ Not supported
├─ Dynamic/personalized content → ✗ Use edge cache only
├─ Need per-request cache control from Workers → ✗ Use R2 directly
└─ Frequently updated content (< 10hr lifetime) → ✗ Not eligible
```

