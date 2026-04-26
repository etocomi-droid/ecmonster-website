## Endpoints

```bash
GET /operations                    # List
GET /operations/{op_id}            # Get single
POST /operations/item              # Create: {endpoint,host,method}
POST /operations                   # Bulk: {operations:[{endpoint,host,method}]}
DELETE /operations/{op_id}         # Delete
DELETE /operations                 # Bulk delete: {operation_ids:[...]}
```

