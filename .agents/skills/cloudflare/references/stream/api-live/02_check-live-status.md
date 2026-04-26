## Check Live Status

```typescript
async function getLiveStatus(accountId: string, liveInputId: string, apiToken: string) {
  const response = await fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/stream/live_inputs/${liveInputId}`,
    { headers: { 'Authorization': `Bearer ${apiToken}` } }
  );
  const { result } = await response.json();
  return {
    isLive: result.status?.current?.state === 'connected',
    recording: result.recording,
    status: result.status
  };
}
```

