## Best Practices

### Security
1. **Never expose API tokens client-side** - Generate participant tokens server-side only
2. **Don't reuse participant tokens** - Generate fresh token per session, use refresh endpoint if expired
3. **Use custom participant IDs** - Map to your user system for cross-session tracking

### Performance
1. **Event-driven updates** - Listen to events, don't poll. Use `toArray()` only when needed
2. **Media quality constraints** - Set appropriate resolution/bitrate limits based on network conditions
3. **Device management** - Enable `autoSwitchAudioDevice` for better UX, handle device list updates

### Architecture
1. **Separate Apps for environments** - staging vs production to prevent data mixing
2. **Preset strategy** - Create presets at App level, reuse across meetings
3. **Token management** - Backend generates tokens, frontend receives via authenticated endpoint

