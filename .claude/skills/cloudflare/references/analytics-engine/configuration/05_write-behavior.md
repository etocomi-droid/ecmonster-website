## Write Behavior

| Scenario | Behavior |
|----------|----------|
| <1M writes/min | All accepted |
| >1M writes/min | Automatic sampling |
| Invalid data | Silent failure (check tail logs) |

**Mitigate sampling:** Pre-aggregate, use multiple datasets, write only critical metrics.

