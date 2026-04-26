## OWASP API Security Top 10 Mapping (2026)

| OWASP Issue | API Shield Solutions |
|-------------|---------------------|
| API1:2023 Broken Object Level Authorization | **BOLA Detection** (enumeration + pollution), Sequence mitigation, Schema, JWT, Rate Limiting |
| API2:2023 Broken Authentication | **Auth Posture**, mTLS, JWT validation, Bot Management |
| API3:2023 Broken Object Property Auth | Schema validation, JWT validation |
| API4:2023 Unrestricted Resource Access | Rate Limiting, **Volumetric Abuse Detection**, **GraphQL Protection**, Bot Management |
| API5:2023 Broken Function Level Auth | Schema validation, JWT validation, Auth Posture |
| API6:2023 Unrestricted Business Flows | Sequence mitigation, Bot Management |
| API7:2023 SSRF | Schema validation, WAF managed rules |
| API8:2023 Security Misconfiguration | **Schema Validation 2.0**, Auth Posture, WAF rules |
| API9:2023 Improper Inventory Management | **API Discovery**, Schema learning, Auth Posture |
| API10:2023 Unsafe API Consumption | JWT validation, Schema validation, WAF managed |

