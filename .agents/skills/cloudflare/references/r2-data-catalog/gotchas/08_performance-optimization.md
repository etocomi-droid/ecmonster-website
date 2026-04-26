## Performance Optimization

### Performance Tips

**Scans:** Use `row_filter` and `selected_fields` to reduce data scanned.  
**Partitions:** 100-1000 optimal. Avoid high cardinality (millions) or low (<10).  
**Files:** Keep 100-500MB avg. Compact if <10MB or >10k files.

