## Component Resources

```typescript
class WorkerApp extends pulumi.ComponentResource {
    constructor(name: string, args: WorkerAppArgs, opts?) {
        super("custom:cloudflare:WorkerApp", name, {}, opts);
        const defaultOpts = {parent: this};

        this.kv = new cloudflare.WorkersKvNamespace(`${name}-kv`, {accountId: args.accountId, title: `${name}-kv`}, defaultOpts);
        this.worker = new cloudflare.WorkerScript(`${name}-worker`, {
            accountId: args.accountId, name: `${name}-worker`, content: args.workerCode,
            module: true, kvNamespaceBindings: [{name: "KV", namespaceId: this.kv.id}],
        }, defaultOpts);
        this.domain = new cloudflare.WorkersDomain(`${name}-domain`, {
            accountId: args.accountId, hostname: args.domain, service: this.worker.name,
        }, defaultOpts);
    }
}
```

