## Advanced

Bandwidth mgmt:
```ts
const s = pc.getSenders().find(s => s.track?.kind === 'video');
const p = s.getParameters();
if (!p.encodings) p.encodings = [{}];
p.encodings[0].maxBitrate = 1200000; p.encodings[0].maxFramerate = 24;
await s.setParameters(p);
```

Simulcast (CF auto-forwards best layer):
```ts
pc.addTransceiver('video', {direction: 'sendonly', sendEncodings: [
  {rid: 'high', maxBitrate: 1200000},
  {rid: 'med', maxBitrate: 600000, scaleResolutionDownBy: 2},
  {rid: 'low', maxBitrate: 200000, scaleResolutionDownBy: 4}
]});
```

DataChannel:
```ts
const dc = pc.createDataChannel('chat', {ordered: true, maxRetransmits: 3});
dc.onopen = () => dc.send(JSON.stringify({type: 'chat', text: 'Hi'}));
dc.onmessage = (e) => console.log('RX:', JSON.parse(e.data));
```

**WHIP/WHEP:** For streaming interop (OBS → SFU, SFU → video players), use WHIP (ingest) and WHEP (egress) protocols. See Cloudflare Stream integration docs.

Integrations: R2 for recording `env.R2_BUCKET.put(...)`, Queues for analytics

Perf: 100-250ms connect, ~50ms latency (95%), 200-400ms glass-to-glass, no participant limit (client: 10-50 tracks)
