### Error Handling

```typescript
app.onError((err, c) => {
  console.error(err);
  return c.json({ error: err.message }, 500);
});

app.notFound((c) => c.json({ error: 'Not Found' }, 404));
```

