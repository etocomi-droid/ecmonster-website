## cf-placement Header (Beta)

Smart Placement adds response header indicating routing decision:

```typescript
// Remote placement (Smart Placement routed request)
"cf-placement: remote-LHR"  // Routed to London

// Local placement (default edge routing)  
"cf-placement: local-EWR"   // Stayed at Newark edge
```

Format: `{placement-type}-{IATA-code}`
- `remote-*` = Smart Placement routed to remote location
- `local-*` = Stayed at default edge location
- IATA code = nearest airport to data center

**Warning:** Beta feature, may be removed before GA.

