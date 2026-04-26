## File-Based Routing

```
/functions/index.ts              → example.com/
/functions/api/users.ts          → example.com/api/users
/functions/api/users/[id].ts     → example.com/api/users/:id
/functions/api/users/[[path]].ts → example.com/api/users/* (catchall)
/functions/_middleware.ts        → Runs before all routes
```

**Rules**: `[param]` = single segment, `[[param]]` = multi-segment catchall, more specific wins.

