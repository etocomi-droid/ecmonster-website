## Expression Syntax

### Fields

```typescript
// Request properties
http.request.method          // GET, POST, etc.
http.request.uri.path        // /api/users
http.host                    // example.com

// IP and Geolocation
ip.src                       // 192.0.2.1
ip.geoip.country            // US, GB, etc.
ip.geoip.continent          // NA, EU, etc.

// Attack detection
cf.waf.score                 // 0-100 attack score
cf.waf.score.sqli           // SQL injection score
cf.waf.score.xss            // XSS score

// Headers & Cookies
http.request.headers["authorization"][0]
http.request.cookies["session"][0]
lower(http.user_agent)      // Lowercase user agent
```

### Operators

```typescript
// Comparison
eq      // Equal
ne      // Not equal
lt      // Less than
le      // Less than or equal
gt      // Greater than
ge      // Greater than or equal

// String matching
contains        // Substring match
matches         // Regex match (use carefully)
starts_with     // Prefix match
ends_with       // Suffix match

// List operations
in              // Value in list
not             // Logical NOT
and             // Logical AND
or              // Logical OR
```

### Expression Examples

```typescript
'cf.waf.score gt 40' // Attack score
'http.request.uri.path eq "/api/login" and http.request.method eq "POST"' // Path + method
'ip.src in {192.0.2.0/24 203.0.113.0/24}' // IP blocking
'ip.geoip.country in {"CN" "RU" "KP"}' // Country blocking
'http.user_agent contains "bot"' // User agent
'not http.request.headers["authorization"][0]' // Header check
'(cf.waf.score.sqli gt 20 or cf.waf.score.xss gt 20) and http.request.uri.path starts_with "/api"' // Complex
```

