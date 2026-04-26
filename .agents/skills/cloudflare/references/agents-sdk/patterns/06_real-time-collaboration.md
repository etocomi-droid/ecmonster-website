## Real-time Collaboration

```ts
export class GameAgent extends Agent<Env> {
  initialState = { players: [], gameStarted: false };
  
  async onConnect(conn: Connection, ctx: ConnectionContext) {
    conn.accept();
    const playerId = ctx.request.headers.get("X-Player-ID") || crypto.randomUUID();
    conn.setState({ playerId });
    
    const newPlayer = { id: playerId, score: 0 };
    this.setState({...this.state, players: [...this.state.players, newPlayer]});
    this.connections.forEach(c => c.send(JSON.stringify({type: "player_joined", player: newPlayer})));
  }
  
  async onMessage(conn: Connection, msg: WSMessage) {
    const m = JSON.parse(msg as string);
    
    if (m.type === "move") {
      this.setState({
        ...this.state,
        players: this.state.players.map(p => p.id === conn.state.playerId ? {...p, score: p.score + m.points} : p)
      });
      this.connections.forEach(c => c.send(JSON.stringify({type: "player_moved", playerId: conn.state.playerId})));
    }
    
    if (m.type === "start" && this.state.players.length >= 2) {
      this.setState({...this.state, gameStarted: true});
      this.connections.forEach(c => c.send(JSON.stringify({type: "game_started"})));
    }
  }
}
```
