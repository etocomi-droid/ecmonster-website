## Request

```javascript
const method = request.method;       // "GET", "POST"
const url = new URL(request.url);    // Parse URL
const headers = request.headers;     // Headers object
const body = await request.json();   // Read body (consumes stream)
const clone = request.clone();       // Clone before reading body

// Query params
url.searchParams.get('page');        // Single value
url.searchParams.getAll('tag');      // Array

// Cloudflare metadata
request.cf.country;                  // "US"
request.cf.colo;                     // "SFO"
```

