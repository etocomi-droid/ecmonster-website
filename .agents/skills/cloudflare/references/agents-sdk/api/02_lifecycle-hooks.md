## Lifecycle Hooks

```ts
onStart() { // Init/restart
  this.sql`CREATE TABLE IF NOT EXISTS users (id TEXT, name TEXT)`;
}

async onRequest(req: Request) { // HTTP
  const {pathname} = new URL(req.url);
  if (pathname === "/users") return Response.json(this.sql<{id,name}>`SELECT * FROM users`);
  return new Response("Not found", {status: 404});
}

async onConnect(conn: Connection<ConnState>, ctx: ConnectionContext) { // WebSocket
  conn.accept();
  conn.setState({userId: ctx.request.headers.get("X-User-ID")});
  conn.send(JSON.stringify({type: "connected", state: this.state}));
}

async onMessage(conn: Connection<ConnState>, msg: WSMessage) { // WS messages
  const m = JSON.parse(msg as string);
  this.setState({messages: [...this.state.messages, m]});
  this.connections.forEach(c => c.send(JSON.stringify(m)));
}

async onEmail(email: AgentEmail) { // Email routing
  this.sql`INSERT INTO emails (from_addr,subject,body) VALUES (${email.from},${email.headers.get("subject")},${await email.text()})`;
}
```

