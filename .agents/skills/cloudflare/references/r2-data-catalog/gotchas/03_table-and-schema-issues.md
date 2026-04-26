## Table and Schema Issues

### Table/Namespace Already Exists

**Error:** `"TableAlreadyExistsError"`  
**Solution:** Use try/except to load existing or check first.

### Namespace Not Found

**Error:** Cannot create table.  
**Solution:** Create namespace first: `catalog.create_namespace("ns")`

### Schema Evolution Errors

**Error:** `"422 Validation"` on schema update.  
**Cause:** Incompatible change (required field, type shrink).  
**Solution:** Only add nullable columns, compatible type widening (int→long, float→double).

