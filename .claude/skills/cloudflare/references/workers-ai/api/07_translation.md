## Translation

```typescript
const result = await env.AI.run('@cf/meta/m2m100-1.2b', {
  text: 'Hello',
  source_lang: 'en',
  target_lang: 'es'
});
console.log(result.translated_text);
```

