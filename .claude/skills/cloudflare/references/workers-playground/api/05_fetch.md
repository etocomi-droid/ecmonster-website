## Fetch

```javascript
const response = await fetch('https://api.example.com');
const data = await response.json();

// With options
await fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Alice' })
});
```

