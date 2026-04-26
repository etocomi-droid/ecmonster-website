## Headers/Redirects Not Working

**Problem**: `_headers` or `_redirects` not applying  
**Causes**: Only work for static assets; Functions override; syntax errors; exceeded limits  
**Solution**: Set headers in Response object for Functions; verify syntax; check limits (100 headers, 2,100 redirects)

