## Security Gotchas

1. **Never expose API token in frontend** - Use direct creator uploads
2. **Always verify webhook signatures** - Prevent spoofed notifications
3. **Set appropriate token expiration** - Short-lived for security
4. **Use requireSignedURLs for private content** - Prevent unauthorized access
5. **Whitelist allowedOrigins** - Prevent hotlinking/embedding on unauthorized sites

