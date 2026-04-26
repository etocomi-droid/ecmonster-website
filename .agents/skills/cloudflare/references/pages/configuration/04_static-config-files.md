## Static Config Files

### _redirects
Place in build output (e.g., `dist/_redirects`):

```txt
/old-page /new-page 301          # 301 redirect
/blog/* /news/:splat 301         # Splat wildcard
/users/:id /members/:id 301      # Placeholders
/api/* /api-v2/:splat 200        # Proxy (no redirect)
```

**Limits**: 2,100 total (2,000 static + 100 dynamic), 1,000 char/line  
**Note**: Functions take precedence

### _headers
```txt
/secure/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff

/api/*
  Access-Control-Allow-Origin: *

/static/*
  Cache-Control: public, max-age=31536000, immutable
```

**Limits**: 100 rules, 2,000 char/line  
**Note**: Only static assets; Functions set headers in Response

### _routes.json
Controls which requests invoke Functions (auto-generated for most frameworks):

```json
{
  "version": 1,
  "include": ["/*"],
  "exclude": ["/build/*", "/static/*", "/assets/*", "/*.{ico,png,jpg,css,js}"]
}
```

**Purpose**: Functions are metered; static requests are free. `exclude` takes precedence. Max 100 rules, 100 char/rule.

