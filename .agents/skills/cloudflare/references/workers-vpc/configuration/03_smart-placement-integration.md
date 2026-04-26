## Smart Placement Integration

Reduce latency by auto-placing Workers near backends:

```jsonc
{ "placement": { "mode": "smart" } }
```

Workers automatically relocate closer to TCP socket destinations after observing connection latency. See [Smart Placement reference](../smart-placement/).

