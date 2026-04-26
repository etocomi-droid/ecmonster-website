## Remote Bindings (Development)

Connect local workerd to production Cloudflare resources:

```capnp
bindings = [
  # Remote KV (requires API token)
  (name = "PROD_KV", kvNamespace = (
    remote = (
      accountId = "your-account-id",
      namespaceId = "your-namespace-id",
      apiToken = .envVar("CF_API_TOKEN")
    )
  )),
  
  # Remote R2
  (name = "PROD_R2", r2Bucket = (
    remote = (
      accountId = "your-account-id",
      bucketName = "my-bucket",
      apiToken = .envVar("CF_API_TOKEN")
    )
  )),
  
  # Remote Durable Object
  (name = "PROD_DO", durableObjectNamespace = (
    remote = (
      accountId = "your-account-id",
      scriptName = "my-worker",
      className = "MyDO",
      apiToken = .envVar("CF_API_TOKEN")
    )
  ))
]
```

**Note:** Remote bindings require network access and valid Cloudflare API credentials.

