## Stage Management (Limit Visible Participants)

```typescript
// Subscribe to top 6 active speakers only
let activeSubscriptions = new Set<string>();

function updateStage(topSpeakers: string[]) {
  const toAdd = topSpeakers.filter(id => !activeSubscriptions.has(id)).slice(0, 6);
  const toRemove = [...activeSubscriptions].filter(id => !topSpeakers.includes(id));
  
  toRemove.forEach(id => {
    pc.getSenders().find(s => s.track?.id === id)?.track?.stop();
    activeSubscriptions.delete(id);
  });
  
  toAdd.forEach(async id => {
    await fetch(`/api/subscribe`, {method: 'POST', body: JSON.stringify({trackId: id})});
    activeSubscriptions.add(id);
  });
}
```

