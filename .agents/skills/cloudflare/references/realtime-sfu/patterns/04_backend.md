## Backend

Express:
```js
app.post('/api/new-session', async (req, res) => {
  const r = await fetch(`${CALLS_API}/apps/${process.env.CALLS_APP_ID}/sessions/new`,
    {method: 'POST', headers: {'Authorization': `Bearer ${process.env.CALLS_APP_SECRET}`}});
  res.json(await r.json());
});
```

Workers: Same pattern, use `env.CALLS_APP_ID` and `env.CALLS_APP_SECRET`

DO Presence: See configuration.md for boilerplate

