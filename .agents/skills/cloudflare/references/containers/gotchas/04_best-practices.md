## Best Practices

1. **Use `startAndWaitForPorts()` by default** - Prevents port errors
2. **Set appropriate `sleepAfter`** - Balance resources vs cold starts
3. **Use `fetch()` for WebSocket** - Not `containerFetch()`
4. **Design for restarts** - Ephemeral disk, implement graceful shutdown
5. **Monitor resources** - Stay within account limits
6. **Keep hooks fast** - Run in `blockConcurrencyWhile`
7. **Renew activity for long ops** - Touch storage to prevent timeout

