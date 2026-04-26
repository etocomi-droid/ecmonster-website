## Create Live Input

### Using Cloudflare SDK

```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({ apiToken: env.CF_API_TOKEN });

const liveInput = await client.stream.liveInputs.create({
  account_id: env.CF_ACCOUNT_ID,
  recording: { mode: 'automatic', timeoutSeconds: 30 },
  deleteRecordingAfterDays: 30
});

// Returns: { uid, rtmps, srt, webRTC }
```

### Raw fetch API

```typescript
async function createLiveInput(accountId: string, apiToken: string) {
  const response = await fetch(
    `https://api.cloudflare.com/client/v4/accounts/${accountId}/stream/live_inputs`,
    {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${apiToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        recording: { mode: 'automatic', timeoutSeconds: 30 },
        deleteRecordingAfterDays: 30
      })
    }
  );
  const { result } = await response.json();
  return {
    uid: result.uid,
    rtmps: { url: result.rtmps.url, streamKey: result.rtmps.streamKey },
    srt: { url: result.srt.url, streamId: result.srt.streamId, passphrase: result.srt.passphrase },
    webRTC: result.webRTC
  };
}
```

