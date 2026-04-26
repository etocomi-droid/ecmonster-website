## Health Checks

Configure via Magic Transit/WAN tunnel endpoints (CNI v2).

```typescript
await client.magicTransit.tunnels.update(accountId, tunnelId, {
  health_check: { enabled: true, target: '192.0.2.1', rate: 'high', type: 'request' },
});
```

Rates: `high` | `medium` | `low`. Types: `request` | `reply`. See [Magic Transit docs](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/#add-tunnels).

