## Debugging Checklist

When things go wrong, check in order:

1. ✅ **Catalog enabled:** `npx wrangler r2 bucket catalog status <bucket>`
2. ✅ **Token permissions:** Both R2 Data Catalog + R2 Storage in dashboard
3. ✅ **Connection test:** `catalog.list_namespaces()` succeeds
4. ✅ **URI format:** HTTPS, includes `/iceberg/`, correct bucket name
5. ✅ **Warehouse name:** Matches bucket name exactly
6. ✅ **Namespace exists:** Create before `create_table()`
7. ✅ **Enable debug logging:** `logging.basicConfig(level=logging.DEBUG)`
8. ✅ **PyIceberg version:** `pip install --upgrade pyiceberg` (≥0.5.0)
9. ✅ **File health:** Compact if >1000 files or avg <10MB
10. ✅ **Snapshot count:** Expire if >100 snapshots

