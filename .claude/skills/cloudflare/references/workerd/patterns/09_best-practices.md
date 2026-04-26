## Best Practices

1. **Use ES modules** over service worker syntax
2. **Explicit bindings** - no global namespace assumptions
3. **Type safety** - define `Env` interfaces (use `wrangler types`)
4. **Service isolation** - split concerns into multiple services
5. **Pin compat date** in production after testing
6. **Use ctx.waitUntil()** for background tasks
7. **Handle errors gracefully** with try/catch
8. **Configure resource limits** on caches/storage

