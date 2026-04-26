## Credential Refresh (Mid-Session)

When credentials expire during long calls:

```typescript
async function refreshTURNCredentials(pc: RTCPeerConnection): Promise<void> {
  const newCreds = await fetch('/turn-credentials').then(r => r.json());
  const config = pc.getConfiguration();
  config.iceServers = newCreds.iceServers;
  pc.setConfiguration(config);
  // Note: setConfiguration() does NOT trigger ICE restart
  // Combine with restartIce() if connection fails
}

// Auto-refresh before expiry
setInterval(async () => {
  await refreshTURNCredentials(peerConnection);
}, 3000000);  // 50 minutes if TTL is 1 hour
```

