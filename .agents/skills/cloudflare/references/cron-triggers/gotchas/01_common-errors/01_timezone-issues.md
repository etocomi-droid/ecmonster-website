### "Timezone Issues"

**Problem:** Cron runs at wrong time relative to local timezone  
**Cause:** All crons execute in UTC, no local timezone support  
**Solution:** Convert local time to UTC manually

**Conversion formula:** `utcHour = (localHour - utcOffset + 24) % 24`

**Examples:**
- 9am PST (UTC-8) → `(9 - (-8) + 24) % 24 = 17` → `0 17 * * *`
- 2am EST (UTC-5) → `(2 - (-5) + 24) % 24 = 7` → `0 7 * * *`
- 6pm JST (UTC+9) → `(18 - 9 + 24) % 24 = 33 % 24 = 9` → `0 9 * * *`

**Daylight Saving Time:** Adjust manually when DST changes, or schedule at times unaffected by DST (e.g., 2am-4am local time usually safe)

