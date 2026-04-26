## Authentication Posture

Identifies unprotected or inconsistently protected endpoints.

**View report:**
```
Security > API Shield > Authentication Posture
- Shows endpoints lacking JWT/mTLS
- Highlights mixed authentication patterns
```

**Remediate:**
1. Review flagged endpoints
2. Add JWT validation rules
3. Configure mTLS for sensitive endpoints
4. Monitor posture score

