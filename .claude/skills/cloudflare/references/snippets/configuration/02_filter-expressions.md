## Filter Expressions

Snippets use Cloudflare's Ruleset Engine expression language to determine when to execute.

### Common Expression Patterns

```javascript
// Host matching
http.host eq "example.com"
http.host in {"example.com" "www.example.com"}
http.host contains "example"

// Path matching
http.request.uri.path eq "/api/users"
starts_with(http.request.uri.path, "/api/")
ends_with(http.request.uri.path, ".json")
matches(http.request.uri.path, "^/api/v[0-9]+/")

// Query parameters
http.request.uri.query contains "debug=true"

// Headers
http.headers["user-agent"] contains "Mobile"
http.headers["accept-language"] eq "en-US"

// Cookies
http.cookie contains "session="

// Geolocation
ip.geoip.country eq "US"
ip.geoip.continent eq "EU"

// Bot detection (requires Bot Management)
cf.bot_management.score lt 30

// Method
http.request.method eq "POST"
http.request.method in {"POST" "PUT" "PATCH"}

// Combine with logical operators
http.host eq "example.com" and starts_with(http.request.uri.path, "/api/")
ip.geoip.country eq "US" or ip.geoip.country eq "CA"
not http.headers["user-agent"] contains "bot"
```

### Expression Functions

| Function | Example | Description |
|----------|---------|-------------|
| `starts_with()` | `starts_with(http.request.uri.path, "/api/")` | Check prefix |
| `ends_with()` | `ends_with(http.request.uri.path, ".json")` | Check suffix |
| `contains()` | `contains(http.headers["user-agent"], "Mobile")` | Check substring |
| `matches()` | `matches(http.request.uri.path, "^/api/")` | Regex match |
| `lower()` | `lower(http.host) eq "example.com"` | Convert to lowercase |
| `upper()` | `upper(http.headers["x-api-key"])` | Convert to uppercase |
| `len()` | `len(http.request.uri.path) gt 100` | String length |

