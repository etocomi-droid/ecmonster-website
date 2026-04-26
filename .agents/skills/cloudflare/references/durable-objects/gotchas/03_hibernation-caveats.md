## Hibernation Caveats

1. **Memory cleared** - All in-memory variables lost; reconstruct from storage or `deserializeAttachment()`
2. **Constructor reruns** - Runs on wake; avoid expensive operations, use lazy initialization
3. **No guarantees** - DO may evict instead of hibernate; design for both
4. **Attachment limit** - `serializeAttachment()` data must be JSON-serializable, keep small
5. **Alarm wakes DO** - Alarm prevents hibernation until handler completes
6. **WebSocket state not automatic** - Must explicitly persist with `serializeAttachment()` or storage

