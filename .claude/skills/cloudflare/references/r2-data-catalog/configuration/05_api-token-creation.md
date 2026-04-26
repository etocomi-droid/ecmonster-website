## API Token Creation

R2 Data Catalog requires API token with **both** R2 Storage + R2 Data Catalog permissions.

### Dashboard Method (Recommended)

1. Go to **R2** → **Manage R2 API Tokens** → **Create API Token**
2. Select permission level:
   - **Admin Read & Write** - Full catalog + storage access (read/write)
   - **Admin Read only** - Read-only access (for query engines)
3. Copy token value immediately (shown only once)

**Permission groups included:**
- `Workers R2 Data Catalog Write` (or Read)
- `Workers R2 Storage Bucket Item Write` (or Read)

### API Method (Programmatic)

Use Cloudflare API to create tokens programmatically. Required permissions:
- `Workers R2 Data Catalog Write` (or Read)
- `Workers R2 Storage Bucket Item Write` (or Read)

