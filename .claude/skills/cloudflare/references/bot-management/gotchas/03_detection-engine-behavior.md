## Detection Engine Behavior

| Engine | Score | Timing | Plan | Notes |
|--------|-------|--------|------|-------|
| Heuristics | Always 1 | Immediate | All | Known fingerprints—overrides ML |
| ML | 1-99 | Immediate | All | Majority of detections |
| Anomaly Detection | Influences | After baseline | Enterprise | Optional, baseline analysis |
| JavaScript Detections | Pass/fail | After JS | Pro+ | Headless browser detection |
| Cloudflare Service | N/A | N/A | Enterprise | Zero Trust internal source |

**Priority:** Heuristics > ML—if heuristic matches, score=1 regardless of ML.

