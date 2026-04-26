## Smart Placement

Automatically optimizes function execution location based on request patterns.

```jsonc
{
  "placement": {
    "mode": "smart"  // Enable optimization (default: off)
  }
}
```

**How it works**: System analyzes traffic over hours/days and places function execution closer to:
- User clusters (e.g., regional traffic)
- Data sources (e.g., D1 database primary location)

**Benefits**: 
- Lower latency for read-heavy apps with centralized databases
- Better performance for apps with regional traffic patterns

**Trade-offs**:
- Initial learning period: First requests may be slower while system optimizes
- Optimization time: Performance improves over 24-48 hours

**When to enable**: Global apps with D1/Durable Objects in specific regions, or apps with concentrated geographic traffic.

**When to skip**: Evenly distributed global traffic with no data locality constraints.

