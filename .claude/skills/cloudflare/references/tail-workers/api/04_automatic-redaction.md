## Automatic Redaction

By default, sensitive data is redacted from `TraceRequest`:

### Header Redaction

Headers containing these substrings (case-insensitive):
- `auth`, `key`, `secret`, `token`, `jwt`
- `cookie`, `set-cookie`

Redacted values show as `"REDACTED"`.

### URL Redaction

- **Hex IDs:** 32+ hex digits → `"REDACTED"`
- **Base-64 IDs:** 21+ chars with 2+ upper, 2+ lower, 2+ digits → `"REDACTED"`

