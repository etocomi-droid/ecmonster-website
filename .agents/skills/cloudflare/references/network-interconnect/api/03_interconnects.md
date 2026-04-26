## Interconnects

```http
GET    /accounts/{account_id}/cni/interconnects              # Query: page, per_page
POST   /accounts/{account_id}/cni/interconnects              # Query: validate_only=true (optional)
GET    /accounts/{account_id}/cni/interconnects/{icon}
GET    /accounts/{account_id}/cni/interconnects/{icon}/status
GET    /accounts/{account_id}/cni/interconnects/{icon}/loa   # Returns PDF
DELETE /accounts/{account_id}/cni/interconnects/{icon}
```

**Create Body:** `account`, `slot_id`, `type`, `facility`, `speed`, `name`, `description`  
**Status Values:** `active` | `healthy` | `unhealthy` | `pending` | `down`

**Response Example:**
```json
{"result": [{"id": "icon_abc", "name": "prod", "type": "direct", "facility": "EWR1", "speed": "10G", "status": "active"}]}
```

