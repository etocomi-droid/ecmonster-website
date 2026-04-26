## Port Exposure

```typescript
// Expose port
const { url } = await sandbox.exposePort(8080, {
  name: 'web-app',
  hostname: request.hostname
});

// Management
await sandbox.isPortExposed(8080);
await sandbox.getExposedPorts(request.hostname);
await sandbox.unexposePort(8080);
```

