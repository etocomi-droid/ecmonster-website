## Status Meanings

**`undefined` (not present)**
- Worker not yet analyzed
- Always runs at default edge location closest to user

**`SUCCESS`**
- Analysis complete, Smart Placement active
- Worker runs in optimal location (may be edge or remote)

**`INSUFFICIENT_INVOCATIONS`**
- Not enough requests to make placement decision
- Requires consistent multi-region traffic
- Always runs at default edge location

**`UNSUPPORTED_APPLICATION`** (rare, <1% of Workers)
- Smart Placement made Worker slower
- Placement decision reverted
- Always runs at edge location
- Won't be re-analyzed until redeployed

