## Limits

| Resource | Limit | Notes |
|----------|-------|-------|
| Cold start | 2-3s | Image pre-fetched globally |
| Graceful shutdown | 15 min | SIGTERM → SIGKILL |
| `start()` timeout | 8s | Process start |
| `startAndWaitForPorts()` timeout | 20s | Port ready |
| Max vCPU per container | 4 | standard-4 or custom |
| Max memory per container | 12 GiB | standard-4 or custom |
| Max disk per container | 20 GB | Ephemeral, resets |
| Account total memory | 400 GiB | All containers |
| Account total vCPU | 100 | All containers |
| Account total disk | 2 TB | All containers |
| Image storage | 50 GB | Per account |
| Disk persistence | None | Use DO storage |

