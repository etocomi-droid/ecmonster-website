## Migrations

```jsonc
{
  "migrations": [
    { "tag": "v1", "new_sqlite_classes": ["MyDO"] },            // Create SQLite (recommended)
    // { "tag": "v1", "new_classes": ["MyDO"] },                // Create KV (paid only)
    { "tag": "v2", "renamed_classes": [{ "from": "Old", "to": "New" }] },
    { "tag": "v3", "transferred_classes": [{ "from": "Src", "from_script": "old", "to": "Dest" }] },
    { "tag": "v4", "deleted_classes": ["Obsolete"] }           // Destroys ALL data!
  ]
}
```

**Migration rules:**
- Tags must be unique and sequential (v1, v2, v3...)
- No rollback supported (test with `--dry-run` first)
- Auto-applied on deploy
- `new_sqlite_classes` recommended over `new_classes` (SQLite vs KV)
- `deleted_classes` immediately destroys ALL data (irreversible)

