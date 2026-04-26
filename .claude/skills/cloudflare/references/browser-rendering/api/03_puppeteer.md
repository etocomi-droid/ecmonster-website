## Puppeteer

```typescript
import puppeteer from "@cloudflare/puppeteer";

const browser = await puppeteer.launch(env.MYBROWSER, { keep_alive: 600000 });
const page = await browser.newPage();
await page.goto('https://example.com', { waitUntil: 'networkidle0' });

// Content
const html = await page.content();
const title = await page.title();

// Screenshot/PDF
await page.screenshot({ fullPage: true, type: 'png' });
await page.pdf({ format: 'A4', printBackground: true });

// Interaction
await page.click('#button');
await page.type('#input', 'text');
await page.evaluate(() => document.querySelector('h1')?.textContent);

// Session management
const sessions = await puppeteer.sessions(env.MYBROWSER);
const limits = await puppeteer.limits(env.MYBROWSER);

await browser.close();
```

