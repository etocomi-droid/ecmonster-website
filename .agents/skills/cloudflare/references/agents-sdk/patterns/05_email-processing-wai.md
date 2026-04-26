## Email Processing w/AI

```ts
export class EmailAgent extends Agent<Env> {
  async onEmail(email: AgentEmail) {
    const [text, from, subject] = [await email.text(), email.from, email.headers.get("subject") || ""];
    this.sql`INSERT INTO emails (from_addr, subject, body) VALUES (${from}, ${subject}, ${text})`;
    
    const { text: summary } = await generateText({
      model: openai("gpt-4o-mini"), prompt: `Summarize: ${subject}\n\n${text}`
    });
    
    this.connections.forEach(c => c.send(JSON.stringify({type: "new_email", from, summary})));
    if (summary.includes("urgent")) await this.schedule(0, "sendAutoReply", { to: from });
  }
}
```

