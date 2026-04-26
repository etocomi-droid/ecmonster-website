## DateTime & Timezone Handling

- All times are **UTC only** (ISO 8601: `"2025-01-15T10:30:00Z"`)
- `Date` type: `"2025-01-15"` (used in `date_geq`/`date_leq` for storage datasets)
- `Time` type: `"2025-01-15T10:30:00Z"` (used in `datetime_gt`/`datetime_lt`)
- Filters are start-inclusive: events that start within the window are included

