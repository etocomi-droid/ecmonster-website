### Proxy Protocol Compatibility

**Problem:** Connection works but app behaves incorrectly  
**Cause:** Origin doesn't support Proxy Protocol

**Solution:**
1. Verify origin supports version (v1: widely supported, v2: HAProxy 1.5+/nginx 1.11+)
2. Test with `proxy_protocol: 'off'` first
3. Configure origin to parse headers

**nginx TCP:**
```nginx
stream {
    server {
        listen 22 proxy_protocol;
        proxy_pass backend:22;
    }
}
```

**HAProxy:**
```
frontend ft_ssh
    bind :22 accept-proxy
```

