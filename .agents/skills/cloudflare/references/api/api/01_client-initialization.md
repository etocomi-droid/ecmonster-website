## Client Initialization

### TypeScript

```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({
  apiToken: process.env.CLOUDFLARE_API_TOKEN,
});
```

### Python

```python
from cloudflare import Cloudflare

client = Cloudflare(api_token=os.environ.get("CLOUDFLARE_API_TOKEN"))

# For async:
from cloudflare import AsyncCloudflare
client = AsyncCloudflare(api_token=os.environ["CLOUDFLARE_API_TOKEN"])
```

### Go

```go
import (
    "github.com/cloudflare/cloudflare-go/v4"
    "github.com/cloudflare/cloudflare-go/v4/option"
)

client := cloudflare.NewClient(
    option.WithAPIToken(os.Getenv("CLOUDFLARE_API_TOKEN")),
)
```

