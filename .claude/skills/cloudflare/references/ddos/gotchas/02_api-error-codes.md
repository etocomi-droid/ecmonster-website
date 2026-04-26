## API Error Codes

| Error Code | Message | Cause | Solution |
|------------|---------|-------|----------|
| 10000 | Authentication error | Invalid/missing API token | Check token has DDoS permissions |
| 81000 | Ruleset validation failed | Invalid rule structure | Verify `action_parameters.id` is managed ruleset ID |
| 81020 | Expression not allowed | Custom expressions on wrong plan | Use `"true"` or upgrade to Enterprise Advanced |
| 81021 | Rule limit exceeded | Too many override rules | Reduce rules or upgrade (Enterprise Advanced: 10) |
| 81022 | Invalid sensitivity level | Wrong sensitivity value | Use: `default`, `medium`, `low`, `eoff` |
| 81023 | Invalid action | Wrong action for plan | Enterprise Advanced only: `log` action |

