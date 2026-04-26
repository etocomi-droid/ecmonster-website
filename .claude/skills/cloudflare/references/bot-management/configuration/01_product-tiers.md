## Product Tiers

**Note:** Dashboard paths differ between old and new UI:
- **New:** Security > Settings > Filter "Bot traffic"
- **Old:** Security > Bots

Both UIs access same settings.

### Bot Score Groupings (Pro/Business)

Pro/Business users see bot score groupings instead of granular 1-99 scores:

| Score | Grouping | Meaning |
|-------|----------|---------|
| 0 | Not computed | Bot Management didn't run |
| 1 | Automated | Definite bot (heuristic match) |
| 2-29 | Likely automated | Probably bot (ML detection) |
| 30-99 | Likely human | Probably human |
| N/A | Verified bot | Allowlisted good bot |

Enterprise plans get granular 1-99 scores for custom thresholds.

### Bot Fight Mode (Free)
- Auto-blocks definite bots (score=1), excludes verified bots by default
- JavaScript Detections always enabled, no configuration options

### Super Bot Fight Mode (Pro/Business)
```txt
Dashboard: Security > Bots > Configure
- Definitely automated: Block/Challenge
- Likely automated: Challenge/Allow  
- Verified bots: Allow (recommended)
- Static resource protection: ON (may block mail clients)
- JavaScript Detections: Optional
```

### Bot Management for Enterprise
```txt
Dashboard: Security > Bots > Configure > Auto-updates: ON (recommended)

# Template 1: Block definite bots
(cf.bot_management.score eq 1 and not cf.bot_management.verified_bot and not cf.bot_management.static_resource)
Action: Block

# Template 2: Challenge likely bots
(cf.bot_management.score ge 2 and cf.bot_management.score le 29 and not cf.bot_management.verified_bot and not cf.bot_management.static_resource)
Action: Managed Challenge
```

