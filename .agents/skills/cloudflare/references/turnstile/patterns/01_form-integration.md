## Form Integration

### Basic Form (Implicit Rendering)

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
</head>
<body>
  <form action="/submit" method="POST">
    <input type="email" name="email" required>
    <div class="cf-turnstile" data-sitekey="YOUR_SITE_KEY"></div>
    <button type="submit">Submit</button>
  </form>
</body>
</html>
```

### Controlled Form (Explicit Rendering)

```javascript
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit"></script>
<script>
let widgetId = window.turnstile.render('#container', {
  sitekey: 'YOUR_SITE_KEY',
  callback: (token) => console.log('Token:', token)
});

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const token = window.turnstile.getResponse(widgetId);
  if (!token) return;
  
  const response = await fetch('/submit', {
    method: 'POST',
    body: JSON.stringify({ 'cf-turnstile-response': token })
  });
  
  if (!response.ok) window.turnstile.reset(widgetId);
});
</script>
```

