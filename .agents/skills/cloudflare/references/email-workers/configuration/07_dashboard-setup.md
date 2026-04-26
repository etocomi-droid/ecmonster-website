## Dashboard Setup

1. **Email Routing:** Domain → Email → Enable Email Routing
2. **Verify addresses:** Email → Destination addresses → Add & verify
3. **Bind Worker:** Email → Email Workers → Create route → Select pattern & Worker
4. **DMARC:** Add TXT `_dmarc.domain.com`: `v=DMARC1; p=quarantine;`

