## Debugging ICE Connectivity

```typescript
pc.addEventListener('icecandidate', (event) => {
  if (event.candidate) {
    console.log('ICE candidate:', event.candidate.type, event.candidate.protocol);
  }
});

pc.addEventListener('iceconnectionstatechange', () => {
  console.log('ICE state:', pc.iceConnectionState);
});

// Check selected candidate pair
const stats = await pc.getStats();
stats.forEach(report => {
  if (report.type === 'candidate-pair' && report.selected) {
    console.log('Selected:', report);
  }
});
```

