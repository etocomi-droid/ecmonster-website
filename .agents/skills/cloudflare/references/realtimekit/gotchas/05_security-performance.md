## Security & Performance

### Security: Do NOT
- Expose `CLOUDFLARE_API_TOKEN` in client code, hardcode credentials in frontend
- Reuse participant tokens, store tokens in localStorage without encryption
- Allow client-side meeting creation

### Security: DO
- Generate tokens server-side only, use HTTPS, implement rate limiting
- Validate user auth before generating tokens, use `custom_participant_id` to map to your user system
- Set appropriate preset permissions per user role, rotate API tokens regularly

### Performance
- **CPU**: Lower video resolution/frameRate, disable video for audio-only, use `meeting.participants.active` for large meetings, implement virtual scrolling
- **Bandwidth**: Set max resolution in `mediaConfiguration`, disable screenshare audio if unneeded, use audio-only mode, implement adaptive bitrate
- **Memory**: Clean up event listeners on unmount, call `meeting.leave()` when done, don't store large participant arrays

