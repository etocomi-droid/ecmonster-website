## Addon System

```typescript
// List available addons
meeting.plugins.all.forEach(plugin => {
  console.log(plugin.id, plugin.name, plugin.active);
});

// Activate collaborative app
await meeting.plugins.activate('whiteboard-addon-id');

// Listen for activations
meeting.plugins.on('pluginActivated', ({ plugin }) => {
  console.log(`${plugin.name} activated`);
});

// Deactivate
await meeting.plugins.deactivate();
```

