## Environment Variables

### Set Variables

| Platform | Command |
|----------|---------|
| Linux/macOS | `export CLOUDFLARE_API_TOKEN='token'` |
| PowerShell | `$env:CLOUDFLARE_API_TOKEN = 'token'` |
| Windows CMD | `set CLOUDFLARE_API_TOKEN=token` |

**Security:** Never commit tokens. Use `.env` files (gitignored) or secret managers.

### .env File Pattern

```bash
# .env (add to .gitignore)
CLOUDFLARE_API_TOKEN=your-token-here
CLOUDFLARE_ACCOUNT_ID=your-account-id
```

```typescript
// TypeScript
import 'dotenv/config';

const client = new Cloudflare({
  apiToken: process.env.CLOUDFLARE_API_TOKEN,
});
```

```python
# Python
from dotenv import load_dotenv
load_dotenv()

client = Cloudflare(api_token=os.environ["CLOUDFLARE_API_TOKEN"])
```

