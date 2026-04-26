## Performance Optimization

### Partitioning
- **Time-series:** day/hour on timestamp
- **Geographic:** region/country
- **Avoid:** High-cardinality keys (user_id)

```python
from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.transforms import DayTransform

PartitionSpec(PartitionField(source_id=1, field_id=1000, transform=DayTransform(), name="day"))
```

### Query Optimization
- **Always use LIMIT** for early termination
- **Filter on partition keys first**
- **Multiple filters** for better pruning

```sql
-- Better: Multiple filters on partition key
SELECT * FROM logs.requests 
WHERE timestamp >= '2025-01-15T00:00:00Z' AND status = 404 AND method = 'GET' LIMIT 100;
```

### File Organization
- **Pipelines roll:** Dev 10-30s, Prod 300+s
- **Target Parquet:** 100-500MB compressed

