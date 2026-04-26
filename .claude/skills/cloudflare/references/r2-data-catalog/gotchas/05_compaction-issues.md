## Compaction Issues

### Compaction Issues

**Problem:** File count unchanged or compaction takes hours.  
**Cause:** Target size too large, or table too big for PyIceberg.  
**Solution:** Only compact if avg <50MB. For >1TB tables, use Spark. Run during low-traffic periods.

