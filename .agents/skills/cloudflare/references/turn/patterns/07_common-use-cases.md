## Common Use Cases

```typescript
// Video conferencing: TURN as fallback
const config = { iceServers: await getTURNConfig(), iceTransportPolicy: 'all' };

// IoT/predictable connectivity: force TURN
const config = { iceServers: await getTURNConfig(), iceTransportPolicy: 'relay' };

// Screen sharing: reduce overhead
const pc = new RTCPeerConnection({ iceServers: await getTURNConfig(), bundlePolicy: 'max-bundle' });
```

