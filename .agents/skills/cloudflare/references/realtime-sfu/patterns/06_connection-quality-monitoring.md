## Connection Quality Monitoring

```typescript
pc.getStats().then(stats => {
  stats.forEach(report => {
    if (report.type === 'inbound-rtp' && report.kind === 'video') {
      const {packetsLost, packetsReceived, jitter} = report;
      const lossRate = packetsLost / (packetsLost + packetsReceived);
      if (lossRate > 0.05) console.warn('High packet loss:', lossRate);
      if (jitter > 100) console.warn('High jitter:', jitter);
    }
  });
});
```

