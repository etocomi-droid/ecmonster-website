## Common Mistakes

### Setting TTL > 48 hours

```typescript
// ❌ BAD: API will reject
const creds = await generate({ ttl: 604800 });  // 7 days

// ✅ GOOD:
const creds = await generate({ ttl: 86400 });   // 24 hours
```

### Hardcoding IPs without monitoring

```typescript
// ❌ BAD: IPs can change with 14-day notice
const iceServers = [{ urls: 'turn:141.101.90.1:3478' }];

// ✅ GOOD: Use DNS
const iceServers = [{ urls: 'turn:turn.cloudflare.com:3478' }];
```

### Using port 53 in browsers

```typescript
// ❌ BAD: Blocked by Chrome/Firefox
urls: ['turn:turn.cloudflare.com:53']

// ✅ GOOD: Filter port 53
urls: urls.filter(url => !url.includes(':53'))
```

### Not handling credential expiry

```typescript
// ❌ BAD: Credentials expire but call continues → connection drops
const creds = await fetchCreds();
const pc = new RTCPeerConnection({ iceServers: creds });

// ✅ GOOD: Refresh before expiry
setInterval(() => refreshCredentials(pc), 3000000);  // 50 min
```

### Missing ICE restart support

```typescript
// ❌ BAD: No recovery from TURN maintenance
pc.addEventListener('iceconnectionstatechange', () => {
  console.log('State changed:', pc.iceConnectionState);
});

// ✅ GOOD: Implement ICE restart
pc.addEventListener('iceconnectionstatechange', async () => {
  if (pc.iceConnectionState === 'failed') {
    await refreshCredentials(pc);
    pc.restartIce();
  }
});
```

### Exposing TURN key secret client-side

```typescript
// ❌ BAD: Secret exposed to client
const secret = 'your-turn-key-secret';
const response = await fetch(`https://rtc.live.cloudflare.com/v1/turn/...`, {
  headers: { 'Authorization': `Bearer ${secret}` }
});

// ✅ GOOD: Generate credentials server-side
const response = await fetch('/api/turn-credentials');
```

