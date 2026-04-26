## Debugging Checklist

1. `npx wrangler r2 bucket catalog enable <bucket>` - Verify catalog
2. `echo $WRANGLER_R2_SQL_AUTH_TOKEN` - Check token
3. `SHOW DATABASES` - List namespaces
4. `SHOW TABLES IN namespace` - List tables
5. `DESCRIBE namespace.table` - Check schema
6. `SELECT COUNT(*) FROM namespace.table` - Verify data
7. `SELECT * FROM namespace.table LIMIT 10` - Test simple query
8. Add filters incrementally

