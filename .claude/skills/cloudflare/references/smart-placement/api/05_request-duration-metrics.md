## Request Duration Metrics

Available in Cloudflare dashboard when Smart Placement enabled:

**Workers & Pages → [Your Worker] → Metrics → Request Duration**

Shows histogram comparing:
- Request duration WITH Smart Placement (99% of traffic)
- Request duration WITHOUT Smart Placement (1% baseline)

**Request Duration vs Execution Duration:**
- **Request duration:** Total time from request arrival to response delivery (includes network latency)
- **Execution duration:** Time Worker code actively executing (excludes network waits)

Use request duration to measure Smart Placement impact.

### Interpreting Metrics

| Metric Comparison | Interpretation | Action |
|-------------------|----------------|--------|
| WITH < WITHOUT | Smart Placement helping | Keep enabled |
| WITH ≈ WITHOUT | Neutral impact | Consider disabling to free resources |
| WITH > WITHOUT | Smart Placement hurting | Disable with `mode: "off"` |

**Why Smart Placement might hurt performance:**
- Worker primarily serves static assets or cached content
- Backend services are globally distributed (no single optimal location)
- Worker has minimal backend communication
- Using Pages with `assets.run_worker_first = true`

**Typical improvements when Smart Placement helps:**
- 20-50% reduction in request duration for database-heavy Workers
- 30-60% reduction for Workers making multiple backend API calls
- Larger improvements when backend is geographically concentrated

