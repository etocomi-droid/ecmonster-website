## TypeScript Types

```typescript
interface CloudflareTURNConfig {
  keyId: string;
  keySecret: string;
  ttl?: number; // Max 172800 (48 hours)
}

interface TURNCredentialsRequest {
  ttl?: number; // Max 172800 seconds
}

interface TURNCredentialsResponse {
  iceServers: {
    urls: string[];
    username: string;
    credential: string;
  };
}

interface RTCIceServer {
  urls: string | string[];
  username?: string;
  credential?: string;
  credentialType?: "password";
}

interface TURNKeyResponse {
  uid: string;
  key: string; // Only present on creation
  name: string;
  created: string;
  modified: string;
}
```

