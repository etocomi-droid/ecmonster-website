## Script Loading

### Basic (Implicit Rendering)
```html
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
```
Automatically renders widgets with `class="cf-turnstile"` on page load.

### Explicit Rendering
```html
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit"></script>
```
Manual control over when/where widgets render via `window.turnstile.render()`.

### With Load Callback
```html
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?onload=myCallback"></script>
<script>
function myCallback() {
  // API ready
  window.turnstile.render('#container', { sitekey: 'YOUR_SITE_KEY' });
}
</script>
```

### Compatibility Mode
```html
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?compat=recaptcha"></script>
```
Provides `grecaptcha` API for Google reCAPTCHA drop-in replacement.

