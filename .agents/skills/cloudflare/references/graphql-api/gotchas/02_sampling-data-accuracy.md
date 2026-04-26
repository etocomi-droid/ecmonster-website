## Sampling & Data Accuracy

### Adaptive Bit Rate (ABR) Sampling

Datasets with `Adaptive` in the name use adaptive sampling:
- Results are **statistically representative**, not exact
- Same query may return **slightly different numbers** each run
- Higher traffic = higher sampling rate = more accurate
- `sampleInterval` dimension shows the ratio (1 = no sampling, 10 = ~1-in-10 sampled)

For high-confidence numbers, use `confidence(level: 0.95)` to get estimate bounds. For exact counts, use rollup nodes (`httpRequests1hGroups`, `httpRequests1dGroups`) which are pre-aggregated without sampling.

### Rollup vs. Adaptive

| Feature | Rollup (`*1hGroups`, `*1dGroups`) | Adaptive (`*AdaptiveGroups`) |
|---------|-----------------------------------|-----------------------------|
| Sampling | No (pre-aggregated) | Yes (ABR) |
| Flexibility | Fixed time buckets | Any granularity |
| Dimensions | Fewer | Many more |
| Accuracy | Exact | Statistical estimate |

