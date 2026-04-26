## Common Errors

| Error | Fix |
|-------|-----|
| "Address not verified" | Add in Email Routing dashboard |
| "Exceeded CPU time" | Use `ctx.waitUntil()` or upgrade |
| "Stream is locked" | Buffer `message.raw` first |
| Silent reply failure | Check DMARC records |
