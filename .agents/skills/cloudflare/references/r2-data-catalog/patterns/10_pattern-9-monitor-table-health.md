## Pattern 9: Monitor Table Health

```python
files = table.scan().plan_files()
avg_mb = sum(f.file_size_in_bytes for f in files) / len(files) / (1024**2)
print(f"Files: {len(files)}, Avg: {avg_mb:.1f}MB, Snapshots: {len(table.snapshots())}")

if avg_mb < 10 or len(files) > 1000:
    print("⚠️ Needs compaction")
```

