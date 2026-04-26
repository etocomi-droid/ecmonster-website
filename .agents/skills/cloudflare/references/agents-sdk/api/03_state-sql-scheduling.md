## State, SQL, Scheduling

```ts
// State
this.setState({count: 42}); // Auto-syncs
this.setState({...this.state, count: this.state.count + 1});

// SQL (parameterized queries prevent injection)
this.sql`CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, name TEXT)`;
this.sql`INSERT INTO users (id,name) VALUES (${userId},${name})`;
const users = this.sql<{id,name}>`SELECT * FROM users WHERE id = ${userId}`;

// Scheduling
await this.schedule(new Date("2026-12-25"), "sendGreeting", {msg:"Hi"}); // Date
await this.schedule(60, "checkStatus", {}); // Delay (sec)
await this.schedule("0 0 * * *", "dailyCleanup", {}); // Cron
await this.cancelSchedule(scheduleId);
```

