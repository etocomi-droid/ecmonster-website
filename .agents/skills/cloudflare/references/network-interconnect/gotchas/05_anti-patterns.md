## Anti-Patterns

| Anti-Pattern | Why Bad | Solution |
|--------------|---------|----------|
| Single interconnect for production | No SLA, single point of failure | Use ≥2 with device diversity |
| No backup Internet | CNI fails = total outage | Always maintain alternate path |
| Polling status every second | Rate limits, wastes API calls | Poll every 30-60s max |
| Using v1 for Magic WAN v2 workloads | GRE overhead, complexity | Use v2 for simplified routing |
| Assuming BGP session = traffic flowing | BGP up ≠ routes installed | Verify routing tables + test traffic |
| Not enabling maintenance alerts | Surprise downtime during maintenance | Enable notifications immediately |
| Hardcoding VLAN in automation | VLAN assigned by CF (v1) | Get VLAN from CNI object response |
| Using Direct without colocation | Can't access cross-connect | Use Partner or Cloud interconnect |

