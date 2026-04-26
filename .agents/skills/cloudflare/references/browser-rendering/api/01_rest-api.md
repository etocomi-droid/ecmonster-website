## REST API

**Base:** `https://api.cloudflare.com/client/v4/accounts/{accountId}/browser-rendering`  
**Auth:** `Authorization: Bearer <token>` (Browser Rendering - Edit permission)

### Endpoints

| Endpoint | Description | Key Options |
|----------|-------------|-------------|
| `/content` | Get rendered HTML | `url`, `waitUntil` |
| `/screenshot` | Capture image | `screenshotOptions: {type, fullPage, clip}` |
| `/pdf` | Generate PDF | `pdfOptions: {format, landscape, margin}` |
| `/snapshot` | HTML + inlined resources | `url` |
| `/scrape` | Extract by selectors | `selectors: ["h1", ".price"]` |
| `/json` | AI-structured extraction | `schema: {name: "string", price: "number"}` |
| `/links` | Get all links | `url` |
| `/markdown` | Convert to markdown | `url` |

```bash
curl -X POST '.../browser-rendering/screenshot' \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"url":"https://example.com","screenshotOptions":{"fullPage":true}}'
```

