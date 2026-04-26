## Security Checklist

- ✅ **Never expose** `CALLS_APP_SECRET` to client
- ✅ **Validate user identity** in backend before creating sessions
- ✅ **Implement auth tokens** for session access (JWT in custom header)
- ✅ **Rate limit** session creation endpoints
- ✅ **Expire sessions** server-side after inactivity
- ✅ **Validate track IDs** before subscribing (prevent unauthorized access)
- ✅ **Use HTTPS** for all signaling (API calls)
- ✅ **Enable DTLS-SRTP** (automatic with Cloudflare, encrypts media)
- ⚠️ **Consider E2EE** for sensitive content (implement client-side with Insertable Streams API)
