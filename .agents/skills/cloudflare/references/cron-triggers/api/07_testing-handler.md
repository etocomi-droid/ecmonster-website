## Testing Handler

**Local development (/__scheduled endpoint):**
```bash
# Start dev server
npx wrangler dev

# Trigger any cron
curl "http://localhost:8787/__scheduled?cron=*/5+*+*+*+*"

# Trigger specific cron with custom time
curl "http://localhost:8787/__scheduled?cron=0+2+*+*+*&scheduledTime=1704067200000"
```

**Query parameters:**
- `cron` - Required. URL-encoded cron expression (use `+` for spaces)
- `scheduledTime` - Optional. Unix timestamp in milliseconds (defaults to current time)

**Production security:** The `/__scheduled` endpoint is available in production and can be triggered by anyone. Block it or implement authentication - see [gotchas.md](./gotchas.md#security-concerns)

**Unit testing (Vitest):**
```typescript
// test/scheduled.test.ts
import { describe, it, expect } from "vitest";
import { env } from "cloudflare:test";
import worker from "../src/index";

describe("Scheduled Handler", () => {
  it("processes scheduled event", async () => {
    const controller = { scheduledTime: Date.now(), cron: "*/5 * * * *", type: "scheduled" as const, noRetry: () => {} };
    const ctx = { waitUntil: (p: Promise<any>) => p, passThroughOnException: () => {} };
    await worker.scheduled(controller, env, ctx);
    expect(await env.MY_KV.get("last_run")).toBeDefined();
  });
  
  it("handles multiple crons", async () => {
    const ctx = { waitUntil: () => {}, passThroughOnException: () => {} };
    await worker.scheduled({ scheduledTime: Date.now(), cron: "*/5 * * * *", type: "scheduled", noRetry: () => {} }, env, ctx);
    expect(await env.MY_KV.get("last_type")).toBe("frequent");
  });
});
```

