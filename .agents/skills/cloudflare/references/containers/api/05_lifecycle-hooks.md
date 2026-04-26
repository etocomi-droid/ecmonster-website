## Lifecycle Hooks

### onStart()

Called when container process starts (ports may not be ready). Runs in `blockConcurrencyWhile` - no concurrent requests.

```typescript
onStart() {
  console.log("Container starting");
}
```

### onStop()

Called when SIGTERM received. 15 minutes until SIGKILL. Use for graceful shutdown.

```typescript
onStop() {
  // Save state, close connections, flush logs
}
```

### onError()

Called when container crashes or fails to start.

```typescript
onError(error: Error) {
  console.error("Container error:", error);
}
```

### onActivityExpired()

Called when `sleepAfter` timeout reached. Return `true` to stay alive, `false` to stop.

```typescript
onActivityExpired(): boolean {
  if (this.hasActiveConnections()) return true;  // Keep alive
  return false;  // OK to stop
}
```

