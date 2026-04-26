## Parent-Child Coordination

Hierarchical DO pattern where parent manages child DOs:

```typescript
// Parent DO coordinates children
export class Workspace extends DurableObject {
  async createDocument(name: string): Promise<string> {
    const docId = crypto.randomUUID();
    const childId = this.env.DOCUMENT.idFromName(`${this.ctx.id.toString()}:${docId}`);
    const childStub = this.env.DOCUMENT.get(childId);
    await childStub.initialize(name);
    
    // Track child in parent storage
    this.sql.exec('INSERT INTO documents (id, name, created) VALUES (?, ?, ?)', 
      docId, name, Date.now());
    return docId;
  }
  
  async listDocuments(): Promise<string[]> {
    return this.sql.exec('SELECT id FROM documents').toArray().map(r => r.id);
  }
}

// Child DO
export class Document extends DurableObject {
  async initialize(name: string) {
    this.sql.exec('CREATE TABLE IF NOT EXISTS content(key TEXT PRIMARY KEY, value TEXT)');
    this.sql.exec('INSERT INTO content VALUES (?, ?)', 'name', name);
  }
}
```

