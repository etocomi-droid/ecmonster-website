## wrangler.jsonc

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "my-cron-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01", // Use current date for new projects
  
  "triggers": {
    "crons": [
      "*/5 * * * *",     // Every 5 minutes
      "0 */2 * * *",     // Every 2 hours
      "0 9 * * MON-FRI", // Weekdays at 9am UTC
      "0 2 1 * *"        // Monthly on 1st at 2am UTC
    ]
  }
}
```

