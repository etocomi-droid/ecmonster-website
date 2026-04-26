## Best Practices

1. **Always close sockets** - Use try/finally blocks
2. **Validate destinations** - Prevent SSRF by allowlisting hosts
3. **Use Hyperdrive for databases** - Better performance than raw TCP
4. **Prefer fetch() for HTTP** - Only use TCP when necessary
5. **Combine with Smart Placement** - Reduce latency to private networks

