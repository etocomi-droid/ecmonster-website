## Best Practices

- Use `startWorker` for integration tests (tests full Worker)
- Use `getPlatformProxy` for unit tests (tests individual functions)
- Use `remote: true` when debugging production-specific issues
- Use `remote: "minimal"` for faster tests with real bindings
- Enable `persist: true` for debugging (state survives runs)
- Run `wrangler types` after config changes
- Always `dispose()` to prevent resource leaks
- Listen to bundle events for build monitoring
- Use multi-worker registry for testing service bindings

