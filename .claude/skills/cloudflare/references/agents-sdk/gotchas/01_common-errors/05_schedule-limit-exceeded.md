### "Schedule limit exceeded"

**Cause:** More than 1000 scheduled tasks per agent
**Solution:** Clean up old schedules and limit creation rate:
```ts
async checkSchedules() { if ((await this.getSchedules()).length > 800) console.warn("Near limit!"); }
```

