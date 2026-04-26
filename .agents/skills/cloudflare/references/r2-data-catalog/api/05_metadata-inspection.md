## Metadata Inspection

```python
table = catalog.load_table(("logs", "app_logs"))
print(table.schema())
print(table.current_snapshot())
print(table.properties)
print(f"Files: {len(table.scan().plan_files())}")
```

