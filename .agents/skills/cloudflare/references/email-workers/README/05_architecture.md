## Architecture

```
Incoming Email → Email Routing → Email Worker
                                    ↓
                              Process + Decide
                                    ↓
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
                Forward          Reply          Reject
```

**Event flow**:
1. Email arrives at your domain
2. Email Routing matches route (e.g., `support@example.com`)
3. Bound Email Worker receives `ForwardableEmailMessage`
4. Worker processes and takes action (forward/reply/reject)
5. Email delivered or rejected based on worker logic

