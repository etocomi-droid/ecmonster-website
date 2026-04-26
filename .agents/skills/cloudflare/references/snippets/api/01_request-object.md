## Request Object

### HTTP Properties
```javascript
request.method    // GET, POST, PUT, DELETE, etc.
request.url       // Full URL string
request.headers   // Headers object
request.body      // ReadableStream (for POST/PUT)
request.cf        // Cloudflare properties (see below)
```

### URL Operations
```javascript
const url = new URL(request.url);
url.hostname             // "example.com"
url.pathname             // "/path/to/page"
url.search               // "?query=value"
url.searchParams.get("q") // "value"
url.searchParams.set("q", "new")
url.searchParams.delete("q")
```

### Header Operations
```javascript
// Read headers
request.headers.get("User-Agent")
request.headers.has("Authorization")
request.headers.getSetCookie() // Get all Set-Cookie headers

// Modify headers (create new request)
const modifiedRequest = new Request(request);
modifiedRequest.headers.set("X-Custom", "value")
modifiedRequest.headers.delete("X-Remove")
```

### Cloudflare Properties (`request.cf`)
Access Cloudflare-specific metadata about the request:

```javascript
// Geolocation
request.cf.city            // "San Francisco"
request.cf.continent       // "NA"
request.cf.country         // "US"
request.cf.region          // "California" or "CA"
request.cf.regionCode      // "CA"
request.cf.postalCode      // "94102"
request.cf.latitude        // "37.7749"
request.cf.longitude       // "-122.4194"
request.cf.timezone        // "America/Los_Angeles"
request.cf.metroCode       // "807" (DMA code)

// Network
request.cf.colo            // "SFO" (airport code of datacenter)
request.cf.asn             // 13335 (ASN number)
request.cf.asOrganization  // "Cloudflare, Inc."

// Bot Management (if enabled)
request.cf.botManagement.score        // 1-99 (1=bot, 99=human)
request.cf.botManagement.verified_bot // true/false
request.cf.botManagement.static_resource // true/false

// TLS/HTTP version
request.cf.tlsVersion      // "TLSv1.3"
request.cf.tlsCipher       // "AEAD-AES128-GCM-SHA256"
request.cf.httpProtocol    // "HTTP/2"

// Request metadata
request.cf.requestPriority // "weight=192;exclusive=0"
```

**Use cases**: Geo-routing, bot detection, security decisions, analytics.

