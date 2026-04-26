## Wrangler Configuration

### Single Tail Consumer

```jsonc
{
  "name": "producer-worker",
  "tail_consumers": [
    {
      "service": "logging-tail-worker"
    }
  ]
}
```

### Multiple Tail Consumers

```jsonc
{
  "name": "producer-worker",
  "tail_consumers": [
    {
      "service": "logging-tail-worker"
    },
    {
      "service": "metrics-tail-worker"
    }
  ]
}
```

**Note:** Each consumer receives ALL events independently.

### Remove Tail Consumer

```jsonc
{
  "tail_consumers": []
}
```

Then redeploy producer Worker.

