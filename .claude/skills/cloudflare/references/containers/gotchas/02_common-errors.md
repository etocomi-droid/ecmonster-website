## Common Errors

### "Container start timeout"

**Cause:** Container took >8s (`start()`) or >20s (`startAndWaitForPorts()`)

**Solutions:**
- Optimize image (smaller base, fewer layers)
- Check `entrypoint` correct
- Verify app listens on correct ports
- Increase timeout if needed

### "Port not available"

**Cause:** Calling `fetch()` before port ready

**Solution:** Use `startAndWaitForPorts()`

### "Container memory exceeded"

**Cause:** Using more memory than instance type allows

**Solutions:**
- Use larger instance type (standard-2, standard-3, standard-4)
- Optimize app memory usage
- Use custom instance type

```jsonc
"instance_type_custom": {
  "vcpu": 2,
  "memory_mib": 8192
}
```

### "Max instances reached"

**Cause:** All `max_instances` slots in use

**Solutions:**
- Increase `max_instances`
- Implement proper `sleepAfter`
- Use `getRandom()` for distribution
- Check for instance leaks

### "No container instance available"

**Cause:** Account capacity limits reached

**Solutions:**
- Check account limits
- Review instance types across containers
- Contact Cloudflare support

