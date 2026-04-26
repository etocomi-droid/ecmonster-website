## REST API Operations

### List Snippets
```bash
GET /zones/{zone_id}/snippets
```

### Get Snippet
```bash
GET /zones/{zone_id}/snippets/{snippet_name}
```

### Create/Update Snippet
```bash
PUT /zones/{zone_id}/snippets/{snippet_name}
Content-Type: multipart/form-data

files=@snippet.js
metadata={"main_module":"snippet.js"}
```

### Delete Snippet
```bash
DELETE /zones/{zone_id}/snippets/{snippet_name}
```

### List Snippet Rules
```bash
GET /zones/{zone_id}/rulesets/phases/http_request_snippets/entrypoint
```

### Update Snippet Rules
```bash
PUT /zones/{zone_id}/snippets/snippet_rules
Content-Type: application/json

{
  "rules": [{
    "description": "Apply snippet",
    "enabled": true,
    "expression": "http.host eq \"example.com\"",
    "snippet_name": "my_snippet"
  }]
}
```

