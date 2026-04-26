## Quick Selection Guide

**Need persistent storage?**
- Key-value < 25MB → **KV**
- Files/objects → **R2**
- Relational data → **D1**
- Real-time coordination → **Durable Objects**

**Need AI/compute?**
- LLM inference → **Workers AI**
- Scraping/PDFs → **Browser Rendering**
- Call another Worker → **Service binding**

**Need async processing?**
- Background jobs → **Queues**

**Need config?**
- Public values → **Environment Variables**
- Secrets → **Secrets** (never commit)

