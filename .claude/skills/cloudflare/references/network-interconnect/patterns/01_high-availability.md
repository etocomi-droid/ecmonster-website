## High Availability

**Critical:** Design for resilience from day one.

**Requirements:**
- Device-level diversity (separate hardware)
- Backup Internet connectivity (no SLA on CNI)
- Network-resilient locations preferred
- Regular failover testing

**Architecture:**
```
Your Network A ──10G CNI v2──> CF CCR Device 1
                                     │
Your Network B ──10G CNI v2──> CF CCR Device 2
                                     │
                            CF Global Network (AS13335)
```

**Capacity Planning:**
- Plan across all links
- Account for failover scenarios
- Your responsibility

