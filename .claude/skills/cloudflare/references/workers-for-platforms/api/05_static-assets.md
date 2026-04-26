## Static Assets

**3-step process:** Create session → Upload files → Deploy Worker

### 1. Create Upload Session
```bash
curl -X POST ".../scripts/$SCRIPT_NAME/assets-upload-session" \
  -H "Authorization: Bearer $API_TOKEN" \
  -d '{
    "manifest": {
      "/index.html": {"hash": "08f1dfda4574284ab3c21666d1ee8c7d4", "size": 1234}
    }
  }'
# Returns: jwt, buckets
```

**Hash:** SHA-256 truncated to first 16 bytes (32 hex characters)

### 2. Upload Files
```bash
curl -X POST ".../workers/assets/upload?base64=true" \
  -H "Authorization: Bearer $UPLOAD_JWT" \
  -F '08f1dfda4574284ab3c21666d1ee8c7d4=<BASE64_CONTENT>'
# Returns: completion jwt
```

**Multiple buckets:** Upload to all returned bucket URLs (typically 2 for redundancy) using same JWT and hash.

### 3. Deploy with Assets
```bash
curl -X PUT ".../scripts/$SCRIPT_NAME" \
  -F 'metadata={
    "main_module": "index.js",
    "assets": {"jwt": "<COMPLETION_TOKEN>"},
    "bindings": [{"type": "assets", "name": "ASSETS"}]
  };type=application/json' \
  -F 'index.js=export default {...};type=application/javascript+module'
```

**Asset Isolation:** Assets shared across namespace by default. For customer isolation, salt hash: `sha256(customerId + fileContents).slice(0, 32)`

