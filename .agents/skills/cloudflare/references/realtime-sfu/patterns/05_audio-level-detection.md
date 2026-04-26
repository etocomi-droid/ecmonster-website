## Audio Level Detection

```typescript
// Attach analyzer to audio track
function attachAudioLevelDetector(track: MediaStreamTrack) {
  const ctx = new AudioContext();
  const analyzer = ctx.createAnalyser();
  const src = ctx.createMediaStreamSource(new MediaStream([track]));
  src.connect(analyzer);
  
  const data = new Uint8Array(analyzer.frequencyBinCount);
  const checkLevel = () => {
    analyzer.getByteFrequencyData(data);
    const level = data.reduce((a, b) => a + b) / data.length;
    if (level > 30) console.log('Speaking:', level); // Trigger UI update
    requestAnimationFrame(checkLevel);
  };
  checkLevel();
}
```

