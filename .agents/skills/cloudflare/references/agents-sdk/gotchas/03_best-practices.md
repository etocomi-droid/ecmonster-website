## Best Practices

### State Management
- Use immutable updates: `setState({...this.state, key: newValue})`
- Trim unbounded arrays (messages, logs) periodically
- Store large data in SQL, not state

### SQL Usage
- Create tables in `onStart()`, not `onRequest()`
- Use parameterized queries: `` sql`WHERE id = ${id}` `` (NOT `` sql`WHERE id = '${id}'` ``)
- Index frequently queried columns

### Scheduling
- Monitor schedule count: `await this.getSchedules()`
- Cancel completed tasks to stay under 1000 limit
- Use cron strings for recurring tasks

### WebSockets
- Always call `conn.accept()` in `onConnect()`
- Handle client disconnects gracefully
- Broadcast to `this.connections` efficiently

### AI Integration
- Use `AIChatAgent` for chat interfaces (auto-streaming, resumption)
- Trim message history to avoid token limits
- Handle AI errors with try/catch and fallbacks

### Production Deployment
- **Rate limiting:** Implement request throttling for high-traffic agents (>1000 req/s)
- **Monitoring:** Log critical errors, track schedule count, monitor storage usage
- **Graceful degradation:** Handle AI service outages with fallbacks
- **Message trimming:** Enforce max history length (e.g., 100 messages) in AIChatAgent
- **MCP reliability:** Re-register servers on hibernation, implement retry logic
