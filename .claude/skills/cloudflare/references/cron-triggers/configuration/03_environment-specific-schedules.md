## Environment-Specific Schedules

```jsonc
{
  "name": "my-cron-worker",
  "triggers": {
    "crons": ["0 */6 * * *"]  // Prod: every 6 hours
  },
  "env": {
    "staging": {
      "triggers": {
        "crons": ["*/15 * * * *"]  // Staging: every 15min
      }
    },
    "dev": {
      "triggers": {
        "crons": ["*/5 * * * *"]  // Dev: every 5min
      }
    }
  }
}
```

