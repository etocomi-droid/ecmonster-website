### Enable Workers Traces

```jsonc
{
  "observability": {
    "traces": {
      "enabled": true,
      "head_sampling_rate": 0.05  // 5% sampling
    }
  }
}
```

**Note**: Default sampling is 100%. For high-traffic Workers, use lower sampling (0.01-0.1).

