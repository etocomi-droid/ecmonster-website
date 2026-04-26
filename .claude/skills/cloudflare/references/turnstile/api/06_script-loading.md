## Script Loading

```html
<!-- Standard -->
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>

<!-- Explicit render mode -->
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit"></script>

<!-- With load callback -->
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?onload=onloadTurnstileCallback"></script>
<script>
window.onloadTurnstileCallback = () => {
  window.turnstile.render('#container', { sitekey: 'YOUR_SITE_KEY' });
};
</script>
```