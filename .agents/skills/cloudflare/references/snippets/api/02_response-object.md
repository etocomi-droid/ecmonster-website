## Response Object

### Response Constructors
```javascript
// Plain text
new Response("Hello", { status: 200 })

// JSON
Response.json({ key: "value" }, { status: 200 })

// HTML
new Response("<h1>Hi</h1>", { 
  status: 200,
  headers: { "Content-Type": "text/html" }
})

// Redirect
Response.redirect("https://example.com", 301) // or 302

// Stream (pass through)
new Response(response.body, response)
```

### Response Headers
```javascript
// Create modified response
const newResponse = new Response(response.body, response);

// Set/modify headers
newResponse.headers.set("X-Custom", "value")
newResponse.headers.append("Set-Cookie", "session=abc; Path=/")
newResponse.headers.delete("Server")

// Common headers
newResponse.headers.set("Cache-Control", "public, max-age=3600")
newResponse.headers.set("Content-Type", "application/json")
```

### Response Properties
```javascript
response.status       // 200, 404, 500, etc.
response.statusText   // "OK", "Not Found", etc.
response.headers      // Headers object
response.body         // ReadableStream
response.ok           // true if status 200-299
response.redirected   // true if redirected
```

