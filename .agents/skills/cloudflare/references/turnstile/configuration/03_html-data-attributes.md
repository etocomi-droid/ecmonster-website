## HTML Data Attributes

For implicit rendering, use data attributes on `<div class="cf-turnstile">`:

| JavaScript Property | HTML Data Attribute | Example |
|---------------------|---------------------|---------|
| `sitekey` | `data-sitekey` | `data-sitekey="YOUR_KEY"` |
| `action` | `data-action` | `data-action="login"` |
| `cData` | `data-cdata` | `data-cdata="session-123"` |
| `callback` | `data-callback` | `data-callback="onSuccess"` |
| `error-callback` | `data-error-callback` | `data-error-callback="onError"` |
| `expired-callback` | `data-expired-callback` | `data-expired-callback="onExpired"` |
| `timeout-callback` | `data-timeout-callback` | `data-timeout-callback="onTimeout"` |
| `theme` | `data-theme` | `data-theme="dark"` |
| `size` | `data-size` | `data-size="compact"` |
| `tabindex` | `data-tabindex` | `data-tabindex="0"` |
| `response-field` | `data-response-field` | `data-response-field="false"` |
| `response-field-name` | `data-response-field-name` | `data-response-field-name="token"` |
| `retry` | `data-retry` | `data-retry="never"` |
| `retry-interval` | `data-retry-interval` | `data-retry-interval="5000"` |
| `language` | `data-language` | `data-language="en"` |
| `execution` | `data-execution` | `data-execution="execute"` |
| `appearance` | `data-appearance` | `data-appearance="interaction-only"` |
| `refresh-expired` | `data-refresh-expired` | `data-refresh-expired="manual"` |

**Example:**
```html
<div class="cf-turnstile"
     data-sitekey="YOUR_SITE_KEY"
     data-theme="dark"
     data-callback="onTurnstileSuccess"
     data-error-callback="onTurnstileError"></div>
```

