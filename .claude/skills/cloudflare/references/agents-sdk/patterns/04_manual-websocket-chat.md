## Manual WebSocket Chat

Custom protocols (non-AI):

```ts
export class ChatAgent extends Agent<Env> {
  async onConnect(conn: Connection, ctx: ConnectionContext) {
    conn.accept();
    conn.setState({userId: ctx.request.headers.get("X-User-ID") || "anon"});
    conn.send(JSON.stringify({type: "history", messages: this.state.messages}));
  }
  
  async onMessage(conn: Connection, msg: WSMessage) {
    const newMsg = {userId: conn.state.userId, text: JSON.parse(msg as string).text, timestamp: Date.now()};
    this.setState({messages: [...this.state.messages, newMsg]});
    this.connections.forEach(c => c.send(JSON.stringify(newMsg)));
  }
}
```

