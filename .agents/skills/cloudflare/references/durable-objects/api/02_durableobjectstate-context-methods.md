## DurableObjectState Context Methods

### Concurrency Control

```typescript
// Complete work after response sent (e.g., cleanup, logging)
this.ctx.waitUntil(promise: Promise<any>): void

// Critical section - blocks all other requests until complete
await this.ctx.blockConcurrencyWhile(async () => {
  // No other requests processed during this block
  // Use for initialization or critical operations
})
```

**When to use:**
- `waitUntil()`: Background cleanup, logging, non-critical work after response
- `blockConcurrencyWhile()`: First-time init, schema migration, critical state setup

### Lifecycle

```typescript
this.ctx.id              // DurableObjectId of this instance
this.ctx.abort()         // Force eviction (use after PITR restore to reload state)
```

### Storage Access

```typescript
this.ctx.storage.sql     // SQLite API (recommended)
this.ctx.storage.kv      // Sync KV API (SQLite DOs only)
this.ctx.storage         // Async KV API (legacy/KV-only DOs)
```

See **[DO Storage](../do-storage/README.md)** for complete storage API reference.

### WebSocket Management

```typescript
this.ctx.acceptWebSocket(ws: WebSocket, tags?: string[])  // Enable hibernation
this.ctx.getWebSockets(tag?: string): WebSocket[]         // Get by tag or all
this.ctx.getTags(ws: WebSocket): string[]                 // Get tags for connection
```

### Alarms

```typescript
await this.ctx.storage.setAlarm(timestamp: number | Date)  // Schedule (overwrites existing)
await this.ctx.storage.getAlarm(): number | null           // Get next alarm time
await this.ctx.storage.deleteAlarm(): void                 // Cancel alarm
```

**Limit:** 1 alarm per DO. Use queue pattern for multiple events (see [Patterns](./patterns.md)).

