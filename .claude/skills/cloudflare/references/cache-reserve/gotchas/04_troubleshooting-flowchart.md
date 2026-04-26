## Troubleshooting Flowchart

Asset not caching in Cache Reserve?

```
1. Is Cache Reserve enabled for zone?
   → No: Enable via Dashboard or API
   → Yes: Continue to step 2

2. Is Tiered Cache enabled?
   → No: Enable Tiered Cache (required!)
   → Yes: Continue to step 3

3. Does asset have TTL ≥ 10 hours?
   → No: Increase via Cache Rules (edge_ttl override)
   → Yes: Continue to step 4

4. Is Content-Length header present?
   → No: Fix origin to include Content-Length
   → Yes: Continue to step 5

5. Is Set-Cookie header present?
   → Yes: Remove Set-Cookie or scope appropriately
   → No: Continue to step 6

6. Is Vary header set to *?
   → Yes: Change to specific value (e.g., Accept-Encoding)
   → No: Continue to step 7

7. Is this a range request?
   → Yes: Range requests bypass Cache Reserve (not supported)
   → No: Continue to step 8

8. Is this an O2O (Orange-to-Orange) request?
   → Yes: O2O bypasses Cache Reserve
   → No: Continue to step 9

9. Check Logpush CacheReserveUsed field
   → Filter logs to see if assets ever hit Cache Reserve
   → Verify cf-cache-status header (should be HIT after first request)
```

