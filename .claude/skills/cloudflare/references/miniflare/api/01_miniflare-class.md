## Miniflare Class

```typescript
class Miniflare {
  constructor(options: MiniflareOptions);
  
  // Lifecycle
  ready: Promise<URL>; // Resolves when server ready, returns URL
  dispose(): Promise<void>; // Cleanup resources
  setOptions(options: MiniflareOptions): Promise<void>; // Reload config
  
  // Event dispatching
  dispatchFetch(url: string | URL | Request, init?: RequestInit): Promise<Response>;
  getWorker(name?: string): Promise<Worker>;
  
  // Bindings access
  getBindings<Bindings = Record<string, unknown>>(name?: string): Promise<Bindings>;
  getCf(name?: string): Promise<IncomingRequestCfProperties | undefined>;
  getKVNamespace(name: string): Promise<KVNamespace>;
  getR2Bucket(name: string): Promise<R2Bucket>;
  getDurableObjectNamespace(name: string): Promise<DurableObjectNamespace>;
  getDurableObjectStorage(id: DurableObjectId): Promise<DurableObjectStorage>;
  getD1Database(name: string): Promise<D1Database>;
  getCaches(): Promise<CacheStorage>;
  getQueueProducer(name: string): Promise<QueueProducer>;
  
  // Debugging
  getInspectorURL(): Promise<URL>; // Chrome DevTools inspector URL
}
```

