## JSON Secret Parsing

Store structured config as JSON secrets:

```typescript
interface Env {
  DB_CONFIG: { get(): Promise<string> };
}

interface DbConfig {
  host: string;
  port: number;
  username: string;
  password: string;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    try {
      const configStr = await env.DB_CONFIG.get();
      const config: DbConfig = JSON.parse(configStr);
      
      // Use parsed config
      const dbUrl = `postgres://${config.username}:${config.password}@${config.host}:${config.port}`;
      
      return Response.json({ connected: true });
    } catch (error) {
      if (error instanceof SyntaxError) {
        return new Response("Invalid config JSON", { status: 500 });
      }
      throw error;
    }
  }
}
```

Store JSON secret:

```bash
echo '{"host":"db.example.com","port":5432,"username":"app","password":"secret"}' | \
  wrangler secrets-store secret create <store-id> \
    --name DB_CONFIG --scopes workers --remote
```

