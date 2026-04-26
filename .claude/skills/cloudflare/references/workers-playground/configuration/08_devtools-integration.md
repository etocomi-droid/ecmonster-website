## DevTools Integration

1. **Open preview** in browser tab
2. **Right-click** → Inspect Element
3. **Console tab** shows Worker logs:
   - `console.log()` output
   - Uncaught errors
   - Network requests (subrequests)

**Note:** DevTools show client-side console, not Worker execution logs. For production logging, use Logpush or Tail Workers.

