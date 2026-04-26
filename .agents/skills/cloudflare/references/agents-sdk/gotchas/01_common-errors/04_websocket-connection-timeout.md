### "WebSocket connection timeout"

**Cause:** Not calling `conn.accept()` in `onConnect`
**Solution:** Always accept connections:
```ts
async onConnect(conn: Connection, ctx: ConnectionContext) { conn.accept(); conn.setState({userId: "123"}); }
```

