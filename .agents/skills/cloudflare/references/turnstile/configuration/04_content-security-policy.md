## Content Security Policy

Add these directives to CSP header/meta tag:

```
script-src https://challenges.cloudflare.com;
frame-src https://challenges.cloudflare.com;
```

**Full Example:**
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' https://challenges.cloudflare.com; 
               frame-src https://challenges.cloudflare.com;">
```

