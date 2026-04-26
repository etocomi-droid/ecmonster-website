## Startup Methods

### start() - Basic start (8s timeout)

```typescript
await container.start();
await container.start({ envVars: { KEY: "value" } });
```

Returns when **process starts**, NOT when ports ready. Use for fire-and-forget.

### startAndWaitForPorts() - Recommended (20s timeout)

```typescript
await container.startAndWaitForPorts();  // Uses requiredPorts
await container.startAndWaitForPorts({ ports: [8080, 9090] });
await container.startAndWaitForPorts({ 
  ports: [8080],
  startOptions: { envVars: { KEY: "value" } }
});
```

Returns when **ports listening**. Use before HTTP/TCP requests.

**Port resolution:** explicit ports → requiredPorts → defaultPort → port 33

### waitForPort() - Wait for specific port

```typescript
await container.waitForPort(8080);
await container.waitForPort(8080, { timeout: 30000 });
```

