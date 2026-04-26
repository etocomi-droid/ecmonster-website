## Rules of Durable Objects

Critical rules preventing most production issues:

1. **One alarm per DO** - Schedule multiple events via queue pattern
2. **~1K req/s per DO max** - Shard for higher throughput
3. **Constructor runs every wake** - Keep initialization light; use lazy loading
4. **Hibernation clears memory** - In-memory state lost; persist critical data
5. **Use `ctx.waitUntil()` for cleanup** - Ensures completion after response sent
6. **No setTimeout for persistence** - Use `setAlarm()` for reliable scheduling

