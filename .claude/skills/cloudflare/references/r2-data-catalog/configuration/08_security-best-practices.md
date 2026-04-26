## Security Best Practices

1. **Store tokens securely** - Use environment variables or secret managers, never hardcode
2. **Use least privilege** - Read-only tokens for query engines, write tokens only where needed
3. **Rotate tokens regularly** - Create new tokens, test, then revoke old ones
4. **One token per application** - Easier to track and revoke if compromised
5. **Monitor token usage** - Check R2 analytics for unexpected patterns
6. **Bucket-scoped tokens** - Create tokens per bucket, not account-wide

