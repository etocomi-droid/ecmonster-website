## Variants Configuration

Variants are named presets for transformations.

### Create Variant (Dashboard)

1. Navigate to Images → Variants
2. Click "Create Variant"
3. Set name (e.g., `thumbnail`)
4. Configure: `width=200,height=200,fit=cover`

### Create Variant (API)

```bash
curl -X POST \
  https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/variants \
  -H "Authorization: Bearer {api_token}" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "thumbnail",
    "options": {
      "width": 200,
      "height": 200,
      "fit": "cover"
    },
    "neverRequireSignedURLs": true
  }'
```

### Use Variant

```
https://imagedelivery.net/{account_hash}/{image_id}/thumbnail
```

### Common Variant Presets

```json
{
  "thumbnail": {
    "width": 200,
    "height": 200,
    "fit": "cover"
  },
  "avatar": {
    "width": 128,
    "height": 128,
    "fit": "cover",
    "gravity": "face"
  },
  "hero": {
    "width": 1920,
    "height": 1080,
    "fit": "cover",
    "quality": 90
  },
  "mobile": {
    "width": 640,
    "fit": "scale-down",
    "quality": 80,
    "format": "avif"
  }
}
```

