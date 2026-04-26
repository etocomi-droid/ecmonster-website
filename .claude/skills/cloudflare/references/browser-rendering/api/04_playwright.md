## Playwright

```typescript
import { launch, connect } from "@cloudflare/playwright";

const browser = await launch(env.MYBROWSER, { keep_alive: 600000 });
const page = await browser.newPage();

await page.goto('https://example.com', { waitUntil: 'networkidle' });

// Modern selectors
await page.locator('.button').click();
await page.getByText('Submit').click();
await page.getByTestId('search').fill('query');

// Context for isolation
const context = await browser.newContext({
  viewport: { width: 1920, height: 1080 },
  userAgent: 'custom'
});

await browser.close();
```

