## Static Config Files

**_routes.json** - Custom routing:
```json
{ "version": 1, "include": ["/api/*"], "exclude": ["/static/*"] }
```

**_headers** - Static headers:
```
/static/*
  Cache-Control: public, max-age=31536000
```

**_redirects** - Redirects:
```
/old  /new  301
```

