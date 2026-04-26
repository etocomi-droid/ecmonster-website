## Basic TURN Configuration (Browser)

```typescript
interface RTCIceServer {
  urls: string | string[];
  username?: string;
  credential?: string;
  credentialType?: "password" | "oauth";
}

async function getTURNConfig(): Promise<RTCIceServer[]> {
  const response = await fetch('/api/turn-credentials');
  const data = await response.json();
  
  return [
    {
      urls: 'stun:stun.cloudflare.com:3478'
    },
    {
      urls: [
        'turn:turn.cloudflare.com:3478?transport=udp',
        'turn:turn.cloudflare.com:3478?transport=tcp',
        'turns:turn.cloudflare.com:5349?transport=tcp',
        'turns:turn.cloudflare.com:443?transport=tcp'
      ],
      username: data.username,
      credential: data.credential,
      credentialType: 'password'
    }
  ];
}

// Use in RTCPeerConnection
const iceServers = await getTURNConfig();
const peerConnection = new RTCPeerConnection({ iceServers });
```

