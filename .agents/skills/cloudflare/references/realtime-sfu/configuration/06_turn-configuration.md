## TURN Configuration

```javascript
const pc = new RTCPeerConnection({
  iceServers: [
    { urls: 'stun:stun.cloudflare.com:3478' },
    {
      urls: [
        'turn:turn.cloudflare.com:3478?transport=udp',
        'turn:turn.cloudflare.com:3478?transport=tcp',
        'turns:turn.cloudflare.com:5349?transport=tcp'
      ],
      username: turnUsername,
      credential: turnCredential
    }
  ],
  bundlePolicy: 'max-bundle', // Recommended: reduces overhead
  iceTransportPolicy: 'all'    // Use 'relay' to force TURN (testing only)
});
```

**Ports:** 3478 (UDP/TCP), 53 (UDP), 80 (TCP), 443 (TLS), 5349 (TLS)

**When to use TURN:** Required for restrictive corporate firewalls/networks that block UDP. ~5-10% of connections fallback to TURN. STUN works for most users.

**ICE candidate filtering:** Cloudflare handles candidate filtering automatically. No need to manually filter candidates.

