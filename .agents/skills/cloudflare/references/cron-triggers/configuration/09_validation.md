## Validation

**Test cron syntax:**
- [crontab.guru](https://crontab.guru/) - Interactive validator
- Wrangler validates on deploy but won't catch logic errors

**Common mistakes:**
- `0 0 * * *` runs daily at midnight UTC, not your local timezone
- `*/60 * * * *` is invalid (use `0 * * * *` for hourly)
- `0 2 31 * *` only runs on months with 31 days

