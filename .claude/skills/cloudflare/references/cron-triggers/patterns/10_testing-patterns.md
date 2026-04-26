## Testing Patterns

**Local testing with /__scheduled:**
```bash
# Start dev server
npx wrangler dev

# Test specific cron
curl "http://localhost:8787/__scheduled?cron=*/5+*+*+*+*"

# Test with specific time
curl "http://localhost:8787/__scheduled?cron=0+2+*+*+*&scheduledTime=1704067200000"
```

**Unit tests:**
```typescript
// test/scheduled.test.ts
import { describe, it, expect, vi } from "vitest";
import { env } from "cloudflare:test";
import worker from "../src/index";

describe("Scheduled Handler", () => {
  it("executes cron", async () => {
    const controller = { scheduledTime: Date.now(), cron: "*/5 * * * *", type: "scheduled" as const, noRetry: vi.fn() };
    const ctx = { waitUntil: vi.fn(), passThroughOnException: vi.fn() };
    await worker.scheduled(controller, env, ctx);
    expect(await env.MY_KV.get("last_run")).toBeDefined();
  });
  
  it("calls noRetry on duplicate", async () => {
    const controller = { scheduledTime: 1704067200000, cron: "0 2 * * *", type: "scheduled" as const, noRetry: vi.fn() };
    await env.EXECUTIONS.put("0 2 * * *-1704067200000", "1");
    await worker.scheduled(controller, env, { waitUntil: vi.fn(), passThroughOnException: vi.fn() });
    expect(controller.noRetry).toHaveBeenCalled();
  });
});
```

