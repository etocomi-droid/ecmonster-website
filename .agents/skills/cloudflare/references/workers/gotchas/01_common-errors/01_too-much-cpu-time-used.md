### "Too much CPU time used"

**Cause:** Worker exceeded CPU time limit (10ms on Free plan, 30s default / 5min max on Paid)  
**Solution:** Use `ctx.waitUntil()` for background work, offload heavy compute to Durable Objects, or consider Workers AI for ML workloads

