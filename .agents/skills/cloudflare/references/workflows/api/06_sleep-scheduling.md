## Sleep & Scheduling

```typescript
// Relative
await step.sleep('wait 1 hour', '1 hour');
await step.sleep('wait 30 days', '30 days');
await step.sleep('wait 5s', 5000); // ms

// Absolute
await step.sleepUntil('launch date', Date.parse('24 Oct 2024 13:00:00 UTC'));
await step.sleepUntil('deadline', new Date('2024-12-31T23:59:59Z'));
```

Units: second, minute, hour, day, week, month, year. Max: 365 days.
Sleeping instances don't count toward concurrency.

