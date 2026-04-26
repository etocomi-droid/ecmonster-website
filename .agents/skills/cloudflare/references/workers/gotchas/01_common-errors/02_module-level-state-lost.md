### "Module-Level State Lost"

**Cause:** Workers are stateless between requests; module-level variables reset unpredictably  
**Solution:** Use KV, D1, or Durable Objects for persistent state; don't rely on module-level variables

