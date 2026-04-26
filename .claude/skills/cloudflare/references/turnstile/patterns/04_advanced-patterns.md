## Advanced Patterns

### Pre-Clearance (Invisible)

```html
<div id="turnstile-precheck"></div>
<form id="protected-form" style="display: none;">
  <button type="submit">Submit</button>
</form>

<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit"></script>
<script>
let cachedToken = null;

window.onload = () => {
  window.turnstile.render('#turnstile-precheck', {
    sitekey: 'YOUR_SITE_KEY',
    size: 'invisible',
    callback: (token) => {
      cachedToken = token;
      document.getElementById('protected-form').style.display = 'block';
    }
  });
};
</script>
```

### Token Refresh on Expiry

```javascript
let widgetId = window.turnstile.render('#container', {
  sitekey: 'YOUR_SITE_KEY',
  'refresh-expired': 'manual',
  'expired-callback': () => {
    console.log('Token expired, refreshing...');
    window.turnstile.reset(widgetId);
  }
});
```

