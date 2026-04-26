## zaraz.track()

```javascript
zaraz.track('button_click');
zaraz.track('purchase', { value: 99.99, currency: 'USD', item_id: '12345' });
zaraz.track('pageview', { page_path: '/products', page_title: 'Products' }); // SPA
```

**Params:** `eventName` (string), `properties` (object, optional). Fire-and-forget.

