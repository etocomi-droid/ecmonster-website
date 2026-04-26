## Error Handling

```javascript
export default {
  async fetch(request) {
    try {
      const response = await fetch('https://api.example.com');
      if (!response.ok) throw new Error(`API returned ${response.status}`);
      return response;
    } catch (error) {
      return Response.json({ error: error.message }, { status: 500 });
    }
  }
};
```

**Note:** In-memory state (Maps, variables) resets on Worker cold start. Use Durable Objects or KV for persistence.
