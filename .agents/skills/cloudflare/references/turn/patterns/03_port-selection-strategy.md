## Port Selection Strategy

Recommended order for browser clients:

1. **3478/udp** (primary, lowest latency)
2. **3478/tcp** (fallback for UDP-blocked networks)
3. **5349/tls** (corporate firewalls, most reliable)
4. **443/tls** (alternate TLS port, firewall-friendly)

**Avoid port 53**—blocked by Chrome and Firefox.

```typescript
function filterICEServersForBrowser(urls: string[]): string[] {
  return urls
    .filter(url => !url.includes(':53'))  // Remove port 53
    .sort((a, b) => {
      // Prioritize UDP over TCP over TLS
      if (a.includes('transport=udp')) return -1;
      if (b.includes('transport=udp')) return 1;
      if (a.includes('transport=tcp') && !a.startsWith('turns:')) return -1;
      if (b.includes('transport=tcp') && !b.startsWith('turns:')) return 1;
      return 0;
    });
}
```

