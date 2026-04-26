## Best Practices

- **ML Auto-Updates**: Enable on Enterprise for latest models
- **Start with Managed Challenge**: Test before blocking
- **Always exclude verified bots**: Use `not cf.bot_management.verified_bot`
- **Exempt corporate proxies**: For B2B traffic via `cf.bot_management.corporate_proxy`
- **Use static resource exception**: Improves performance, reduces overhead
