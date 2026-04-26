## Timeout Environment Overrides

Override default timeouts via environment variables:

```jsonc
{
  "vars": {
    "SANDBOX_INSTANCE_TIMEOUT_MS": "60000",  // Override instanceGetTimeoutMS
    "SANDBOX_PORT_TIMEOUT_MS": "120000"      // Override portReadyTimeoutMS
  }
}
```
