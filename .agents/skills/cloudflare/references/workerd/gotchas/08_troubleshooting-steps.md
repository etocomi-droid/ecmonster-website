## Troubleshooting Steps

1. **Enable verbose logging**: `workerd serve config.capnp --verbose`
2. **Check logs**: Look for error messages, stack traces
3. **Validate config**: `capnp compile -I. config.capnp`
4. **Test bindings**: Log `Object.keys(env)` to verify
5. **Check versions**: Workerd version vs compat date
6. **Isolate issue**: Minimal repro config
7. **Review schema**: [workerd.capnp](https://github.com/cloudflare/workerd/blob/main/src/workerd/server/workerd.capnp)

See [configuration.md](./configuration.md) for config details, [patterns.md](./patterns.md) for working examples, [api.md](./api.md) for runtime APIs.
