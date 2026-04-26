## Discovery

```bash
GET /discovery/operations                    # List discovered
PATCH /discovery/operations/{op_id}          # Update: {state:"saved"|"ignored"}
PATCH /discovery/operations                  # Bulk: {operation_ids:{id:{state}}}
GET /discovery                               # OpenAPI export
```

