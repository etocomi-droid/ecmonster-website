## HTMLRewriter

```typescript
return new HTMLRewriter()
  .on('a[href]', {
    element(el) {
      const href = el.getAttribute('href');
      if (href?.startsWith('http://')) {
        el.setAttribute('href', href.replace('http://', 'https://'));
      }
    }
  })
  .transform(response);
```

**Use cases**: A/B testing, analytics injection, link rewriting

