## Preview Panel

### Browser Tab

Default interactive preview with address bar:
- Enter custom URL paths
- Automatic reload on code changes
- DevTools available (right-click → Inspect)

### HTTP Test Panel

Switch to **HTTP** tab for raw HTTP testing:
- Change HTTP method (GET, POST, PUT, DELETE, PATCH, etc.)
- Add/edit request headers
- Modify request body (JSON, form data, text)
- View response headers and body
- Test different content types

Example HTTP test:
```
Method: POST
URL: /api/users
Headers:
  Content-Type: application/json
  Authorization: Bearer token123
Body:
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

