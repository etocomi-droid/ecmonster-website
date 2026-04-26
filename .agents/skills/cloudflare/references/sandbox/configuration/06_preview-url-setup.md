## Preview URL Setup

**Prerequisites**:
- Custom domain with wildcard DNS: `*.yourdomain.com → worker.yourdomain.com`
- `.workers.dev` domains NOT supported
- `normalizeId: true` in getSandbox
- `proxyToSandbox()` called first in fetch handler

