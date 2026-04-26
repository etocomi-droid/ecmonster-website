## In-Memory Caching

```typescript
export class UserCache extends DurableObject {
  cache = new Map<string, User>();
  async getUser(id: string): Promise<User | undefined> {
    if (this.cache.has(id)) {
      const cached = this.cache.get(id);
      if (cached) return cached;
    }
    const user = await this.ctx.storage.get<User>(`user:${id}`);
    if (user) this.cache.set(id, user);
    return user;
  }
  async updateUser(id: string, data: Partial<User>) {
    const updated = { ...await this.getUser(id), ...data };
    this.cache.set(id, updated);
    await this.ctx.storage.put(`user:${id}`, updated);
    return updated;
  }
}
```

