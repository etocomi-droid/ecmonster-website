## Async Behavior

All methods fire-and-forget. Events batched and sent asynchronously:

```javascript
zaraz.track('event1');
zaraz.set('prop', 'value');
zaraz.track('event2'); // All batched
```

