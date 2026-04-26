## Troubleshooting

### "Token authentication failed"

**Cause:** Invalid or missing token

**Solution:**
- Verify `WRANGLER_R2_SQL_AUTH_TOKEN` environment variable set
- Check token has Admin Read & Write permission
- Create new token if expired

### "Catalog not enabled on bucket"

**Cause:** Data Catalog not enabled

**Solution:**
- Run `npx wrangler r2 bucket catalog enable <bucket-name>`
- Or enable via Dashboard (R2 → bucket → Settings → R2 Data Catalog)

### "Permission denied"

**Cause:** Token lacks required permissions

**Solution:**
- Verify token has **Admin Read & Write** permission
- Create new token with correct permissions

