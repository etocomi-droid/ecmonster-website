## Smart Placement Issues

### Increased Cold Start Latency

**Problem**: First requests slower after enabling Smart Placement  
**Cause**: Initial optimization period while system learns traffic patterns  
**Solution**: Expected behavior during first 24-48 hours; monitor latency trends over time

### Inconsistent Response Times

**Problem**: Latency varies significantly across requests during initial deployment  
**Cause**: Smart Placement testing different execution locations to find optimal placement  
**Solution**: Normal during learning phase; stabilizes after traffic patterns emerge (1-2 days)

### No Performance Improvement

**Problem**: Smart Placement enabled but no latency reduction observed  
**Cause**: Traffic evenly distributed globally, or no data locality constraints  
**Solution**: Smart Placement most effective with centralized data (D1/DO) or regional traffic; disable if no benefit

