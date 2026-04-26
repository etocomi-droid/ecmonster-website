## WAF Integration Points

- **WAF Custom Rules**: Primary enforcement mechanism
- **Rate Limiting Rules**: Bot score as dimension, stricter limits for low scores
- **Transform Rules**: Pass score to origin via custom header
- **Workers**: Programmatic bot logic, custom scoring algorithms
- **Page Rules / Configuration Rules**: Zone-level overrides, path-specific settings

