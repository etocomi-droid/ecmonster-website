### "WebSockets Disconnect on Eviction"

**Problem:** Connections drop unexpectedly  
**Cause:** DO evicted from memory without hibernation API  
**Solution:** Use WebSocket hibernation handlers + client reconnection logic

