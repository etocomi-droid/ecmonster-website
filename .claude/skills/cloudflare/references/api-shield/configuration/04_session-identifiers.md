## Session Identifiers

Critical for BOLA Detection, Sequence Mitigation, and analytics. Configure header/cookie that uniquely IDs API users.

**Examples:** JWT sub claim, session token, API key, custom user ID header

**Configure:**
```
Security > API Shield > Settings > Session Identifiers
- Type: Header/Cookie
- Name: "X-User-ID" or "Authorization"
```

