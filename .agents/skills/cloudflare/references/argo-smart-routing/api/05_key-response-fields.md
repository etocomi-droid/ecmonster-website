## Key Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `value` | `"on" \| "off"` | Current enablement status |
| `editable` | `boolean` | Whether changes are allowed (check before PATCH) |
| `modified_on` | `string` | ISO timestamp of last modification |
| `success` | `boolean` | Whether request succeeded |
| `errors` | `Array` | Error details if `success: false`