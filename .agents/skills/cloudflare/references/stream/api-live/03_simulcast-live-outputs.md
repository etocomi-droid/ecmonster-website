## Simulcast (Live Outputs)

### Create Output

```typescript
async function createLiveOutput(
  accountId: string, liveInputId: string, apiToken: string,
  outputUrl: string, streamKey: string
) {
  return fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/stream/live_inputs/${liveInputId}/outputs`,
    {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${apiToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        url: `${outputUrl}/${streamKey}`,
        enabled: true,
        streamKey // For platforms like YouTube, Twitch
      })
    }
  ).then(r => r.json());
}
```

### Example: Simulcast to YouTube + Twitch

```typescript
const liveInput = await createLiveInput(accountId, apiToken);

// Add YouTube output
await createLiveOutput(
  accountId, liveInput.uid, apiToken,
  'rtmp://a.rtmp.youtube.com/live2',
  'your-youtube-stream-key'
);

// Add Twitch output
await createLiveOutput(
  accountId, liveInput.uid, apiToken,
  'rtmp://live.twitch.tv/app',
  'your-twitch-stream-key'
);
```

