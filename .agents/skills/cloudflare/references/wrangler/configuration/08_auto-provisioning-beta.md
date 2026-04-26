## Auto-Provisioning (Beta)

Omit resource IDs - Wrangler creates them and writes back to config on deploy.

```jsonc
{ "kv_namespaces": [{ "binding": "MY_KV" }] }  // No id - auto-provisioned
```

After deploy, ID is added to config automatically.

