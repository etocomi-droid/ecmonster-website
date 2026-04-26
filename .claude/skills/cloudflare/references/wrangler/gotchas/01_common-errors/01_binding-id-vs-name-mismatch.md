### "Binding ID vs name mismatch"

**Cause:** Confusion between binding name (code) and resource ID
**Solution:** Bindings use `binding` (code name) and `id`/`database_id`/`bucket_name` (resource ID). Preview bindings need separate IDs: `preview_id`, `preview_database_id`

