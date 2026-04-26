## TypeScript Types

**env.d.ts:**
```typescript
interface Env {
  MY_KV: KVNamespace;
  SESSIONS: KVNamespace;
  CACHE: KVNamespace;
}
```

**worker.ts:**
```typescript
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    // env.MY_KV is now typed as KVNamespace
    const value = await env.MY_KV.get("key");
    return new Response(value || "Not found");
  }
} satisfies ExportedHandler<Env>;
```

**Type-safe JSON operations:**
```typescript
interface UserProfile {
  name: string;
  email: string;
  role: "admin" | "user";
}

const profile = await env.USERS.get<UserProfile>("user:123", "json");
// profile: UserProfile | null (type-safe!)
if (profile) {
  console.log(profile.name); // TypeScript knows this is a string
}
```

