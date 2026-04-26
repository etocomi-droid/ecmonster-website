## Common Errors

### "Cannot connect to meeting"

**Cause:** Auth token invalid/expired, API credentials lack permissions, or network blocks WebRTC
**Solution:**
Verify token validity, check API token has **Realtime / Realtime Admin** permissions, enable TURN service for restrictive networks

### "No video/audio tracks"

**Cause:** Browser permissions not granted, video/audio not enabled, device in use, or device unavailable
**Solution:**
Request browser permissions explicitly, verify initialization config, use `meeting.self.getAllDevices()` to debug, close other apps using device

### "Participant count mismatched"

**Cause:** `meeting.participants` doesn't include `meeting.self`
**Solution:** Total count = `meeting.participants.joined.size() + 1`

### "Events not firing"

**Cause:** Listeners registered after actions, incorrect event name, or wrong namespace
**Solution:**
Register listeners before calling `meeting.join()`, check event names against docs, verify correct namespace

### "CORS errors in API calls"

**Cause:** Making REST API calls from client-side
**Solution:** All REST API calls **must** be server-side (Workers, backend). Never expose API tokens to clients.

### "Preset not applying"

**Cause:** Preset doesn't exist, name mismatch (case-sensitive), or participant created before preset
**Solution:**
Verify preset exists via Dashboard or API, check exact spelling and case, create preset before adding participants

### "Token reuse error"

**Cause:** Reusing participant tokens across sessions
**Solution:** Generate fresh token per session. Use refresh endpoint if token expires during session.

### "Video quality poor"

**Cause:** Insufficient bandwidth, resolution/bitrate too high, or CPU overload
**Solution:**
Lower `mediaConfiguration.video` resolution/frameRate, monitor network conditions, reduce participant count or grid size

### "Echo or audio feedback"

**Cause:** Multiple devices picking up same audio source
**Solution:**
- Lower `mediaConfiguration.video` resolution/frameRate
- Monitor network conditions
- Reduce participant count or grid size

### Issue: Echo or audio feedback
**Cause**: Multiple devices picking up same audio source

**Solutions**:
Enable `echoCancellation: true` in `mediaConfiguration.audio`, use headphones, mute when not speaking

### "Screen share not working"

**Cause:** Browser doesn't support screen sharing API, permission denied, or wrong `displaySurface` config
**Solution:**
Use Chrome/Edge/Firefox (Safari limited support), check browser permissions, try different `displaySurface` values ('window', 'monitor', 'browser')

### "How do I schedule meetings?"

**Cause:** RealtimeKit has no built-in scheduling system
**Solution:**
Store meeting IDs in your database with timestamps. Generate participant tokens only when user should join. Example:
```typescript
// Store in DB
{ meetingId: 'abc123', scheduledFor: '2026-02-15T10:00:00Z', userId: 'user456' }

// Generate token when user clicks "Join" near scheduled time
const response = await fetch('/api/join-meeting', {
  method: 'POST',
  body: JSON.stringify({ meetingId: 'abc123' })
});
const { authToken } = await response.json();
```

### "Recording not starting"

**Cause:** Preset lacks recording permissions, no active session, or API call from client
**Solution:**
Verify preset has `canRecord: true` and `canStartStopRecording: true`, ensure session is active (at least one participant), make recording API calls server-side only

