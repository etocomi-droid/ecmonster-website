## Troubleshooting

### Video stuck in "inprogress" state
- **Cause**: Processing large/complex video
- **Solution**: Wait up to 5 minutes for processing; use webhooks instead of polling

### Signed URL returns 403
- **Cause**: Token expired or invalid signature
- **Solution**: Check expiration timestamp, verify JWK is correct, ensure clock sync

### Live stream not connecting
- **Cause**: Invalid RTMPS URL or stream key
- **Solution**: Use exact URL/key from API, ensure firewall allows outbound 443

### Webhook signature verification fails
- **Cause**: Incorrect secret or timestamp window
- **Solution**: Use exact secret from webhook setup, allow 5-minute timestamp drift

### Video uploads but isn't visible
- **Cause**: `requireSignedURLs` enabled without providing token
- **Solution**: Generate signed token or set `requireSignedURLs: false` for public videos

### Player shows infinite loading
- **Cause**: CORS issue with allowedOrigins
- **Solution**: Add your domain to `allowedOrigins` array

