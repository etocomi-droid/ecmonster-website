### 9. Deployment Order

**Problem:** Producer deployment fails  
**Cause:** Tail consumer not deployed yet  
**Solution:** Deploy tail consumer FIRST

```bash
cd tail-worker && wrangler deploy
cd ../producer && wrangler deploy
```

