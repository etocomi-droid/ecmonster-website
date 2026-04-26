## TURN Key Management

### List TURN Keys

```
GET /accounts/{account_id}/calls/turn_keys
```

### Get TURN Key Details

```
GET /accounts/{account_id}/calls/turn_keys/{key_id}
```

### Create TURN Key

```
POST /accounts/{account_id}/calls/turn_keys
Content-Type: application/json

{
  "name": "my-turn-key"
}
```

**Response includes**:
- `uid`: Key identifier
- `key`: The actual secret key (only returned on creation—save immediately)
- `name`: Human-readable name
- `created`: ISO 8601 timestamp
- `modified`: ISO 8601 timestamp

### Update TURN Key

```
PUT /accounts/{account_id}/calls/turn_keys/{key_id}
Content-Type: application/json

{
  "name": "updated-name"
}
```

### Delete TURN Key

```
DELETE /accounts/{account_id}/calls/turn_keys/{key_id}
```

