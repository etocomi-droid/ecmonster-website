## wrangler.toml Format

```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2026-01-10"

[[containers]]
class_name = "MyContainer"
image = "./Dockerfile"
instance_type = "standard-2"
max_instances = 10

[[durable_objects.bindings]]
name = "MY_CONTAINER"
class_name = "MyContainer"

[[migrations]]
tag = "v1"
new_sqlite_classes = ["MyContainer"]
```

Both `wrangler.jsonc` and `wrangler.toml` are supported. Use `wrangler.jsonc` for comments and better IDE support.
