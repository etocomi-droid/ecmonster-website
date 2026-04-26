## Green Compute (Beta)

Schedule crons during low-carbon periods for carbon-aware execution:

```jsonc
{
  "name": "eco-cron-worker",
  "triggers": {
    "crons": ["0 2 * * *"]
  },
  "placement": {
    "mode": "smart"  // Runs during low-carbon periods
  }
}
```

**Modes:**
- `"smart"` - Carbon-aware scheduling (may delay up to 24h for optimal window)
- Default (no placement config) - Standard scheduling (no delay)

**How it works:**
- Cloudflare delays execution until grid carbon intensity is lower
- Maximum delay: 24 hours from scheduled time
- Ideal for batch jobs with flexible timing requirements

**Use cases:** 
- Nightly data processing and ETL pipelines
- Weekly/monthly report generation
- Database backups and maintenance
- Analytics aggregation
- ML model training

**Not suitable for:** 
- Time-sensitive operations (SLA requirements)
- User-facing features requiring immediate execution
- Real-time monitoring and alerting
- Compliance tasks with strict time windows

