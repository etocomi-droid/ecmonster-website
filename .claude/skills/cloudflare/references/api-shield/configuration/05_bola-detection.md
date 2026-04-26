## BOLA Detection

Detects Broken Object Level Authorization attacks (enumeration + parameter pollution).

**Enable:**
```
Security > API Shield > Schema Validation > [Select Schema] > BOLA Detection
- Enable detection
- Threshold: Sensitivity level (Low/Medium/High)
- Action: Log or Block
```

**Requirements:**
- Schema Validation 2.0 enabled
- Session identifiers configured
- Minimum traffic: 1000+ requests/day per endpoint

