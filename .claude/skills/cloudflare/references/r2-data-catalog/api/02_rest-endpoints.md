## REST Endpoints

Base: `https://<account-id>.r2.cloudflarestorage.com/iceberg/<bucket-name>`

| Operation | Method | Path |
|-----------|--------|------|
| Catalog config | GET | `/v1/config` |
| List namespaces | GET | `/v1/namespaces` |
| Create namespace | POST | `/v1/namespaces` |
| Delete namespace | DELETE | `/v1/namespaces/{ns}` |
| List tables | GET | `/v1/namespaces/{ns}/tables` |
| Create table | POST | `/v1/namespaces/{ns}/tables` |
| Load table | GET | `/v1/namespaces/{ns}/tables/{table}` |
| Update table | POST | `/v1/namespaces/{ns}/tables/{table}` |
| Delete table | DELETE | `/v1/namespaces/{ns}/tables/{table}` |
| Rename table | POST | `/v1/tables/rename` |

**Authentication:** Bearer token in header: `Authorization: Bearer <token>`

