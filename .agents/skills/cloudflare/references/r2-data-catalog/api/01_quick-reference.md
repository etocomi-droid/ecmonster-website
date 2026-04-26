## Quick Reference

**Most common operations:**

| Task | PyIceberg Code |
|------|----------------|
| Connect | `RestCatalog(name="r2", warehouse=bucket, uri=uri, token=token)` |
| List namespaces | `catalog.list_namespaces()` |
| Create namespace | `catalog.create_namespace("logs")` |
| Create table | `catalog.create_table(("ns", "table"), schema=schema)` |
| Load table | `catalog.load_table(("ns", "table"))` |
| Append data | `table.append(pyarrow_table)` |
| Query data | `table.scan().to_pandas()` |
| Compact files | `table.rewrite_data_files(target_file_size_bytes=128*1024*1024)` |
| Expire snapshots | `table.expire_snapshots(older_than=timestamp_ms, retain_last=10)` |

