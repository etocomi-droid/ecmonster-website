## Workers for Platforms

For dynamic dispatch Workers, both dispatch and user Worker events sent to tail consumer:

```jsonc
{
  "name": "dispatch-worker",
  "tail_consumers": [
    {
      "service": "platform-tail-worker"
    }
  ]
}
```

Tail Worker receives TWO `TraceItem` elements per request:
1. Dynamic dispatch Worker event
2. User Worker event

See [patterns.md](patterns.md) for handling.
