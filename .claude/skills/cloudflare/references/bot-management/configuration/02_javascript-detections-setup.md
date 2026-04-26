## JavaScript Detections Setup

### Enable via Dashboard
```txt
Security > Bots > Configure Bot Management > JS Detections: ON

Update CSP: script-src 'self' /cdn-cgi/challenge-platform/;
```

### Manual JS Injection (API)
```html
<script>
function jsdOnload() {
  window.cloudflare.jsd.executeOnce({ callback: function(result) { console.log('JSD:', result); } });
}
</script>
<script src="/cdn-cgi/challenge-platform/scripts/jsd/api.js?onload=jsdOnload" async></script>
```

**Use API for**: Selective deployment on specific pages  
**Don't combine**: Zone-wide toggle + manual injection

### WAF Rules for JSD
```txt
# NEVER use on first page visit (needs HTML page first)
(not cf.bot_management.js_detection.passed and http.request.uri.path eq "/api/user/create" and http.request.method eq "POST" and not cf.bot_management.verified_bot)
Action: Managed Challenge (always use Managed Challenge, not Block)
```

### Limitations
- First request won't have JSD data (needs HTML page first)
- Strips ETags from HTML responses
- Not supported with CSP via `<meta>` tags
- Websocket endpoints not supported
- Native mobile apps won't pass
- cf_clearance cookie: 15-minute lifespan, max 4096 bytes

