## Hyperdrive Integration

For PostgreSQL/MySQL, prefer Hyperdrive over raw TCP sockets (includes connection pooling):

```jsonc
{ "hyperdrive": [{ "binding": "DB", "id": "<HYPERDRIVE_ID>" }] }
```

See [Hyperdrive reference](../hyperdrive/) for complete setup.

