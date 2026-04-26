## REST API

Base: `https://api.cloudflare.com/client/v4/accounts/{account_id}/realtime/kit/{app_id}`

### Meetings
```bash
GET    /meetings                                    # List all
GET    /meetings/{meeting_id}                       # Get details
POST   /meetings                                    # Create: {"title": "..."}
PATCH  /meetings/{meeting_id}                       # Update: {"title": "...", "record_on_start": true}
```

### Participants
```bash
GET    /meetings/{meeting_id}/participants                          # List all
GET    /meetings/{meeting_id}/participants/{participant_id}         # Get details
POST   /meetings/{meeting_id}/participants                          # Add: {"name": "...", "preset_name": "...", "custom_participant_id": "..."}
PATCH  /meetings/{meeting_id}/participants/{participant_id}         # Update: {"name": "...", "preset_name": "..."}
DELETE /meetings/{meeting_id}/participants/{participant_id}         # Delete
POST   /meetings/{meeting_id}/participants/{participant_id}/token   # Refresh token
```

### Active Session
```bash
GET  /meetings/{meeting_id}/active-session               # Get active session
POST /meetings/{meeting_id}/active-session/kick          # Kick users: {"user_ids": ["id1", "id2"]}
POST /meetings/{meeting_id}/active-session/kick-all      # Kick all
POST /meetings/{meeting_id}/active-session/poll          # Create poll: {"question": "...", "options": [...], "anonymous": false}
```

### Recording
```bash
GET  /recordings?meeting_id={meeting_id}                 # List recordings
GET  /recordings/active-recording/{meeting_id}           # Get active recording
POST /recordings                                         # Start: {"meeting_id": "...", "type": "composite"} (or "track")
PUT  /recordings/{recording_id}                          # Control: {"action": "pause"} (or "resume", "stop")
POST /recordings/track                                   # Track recording: {"meeting_id": "...", "layers": [...]}
```

### Livestreaming
```bash
GET  /livestreams?exclude_meetings=false                                # List all
GET  /livestreams/{livestream_id}                                       # Get details
POST /meetings/{meeting_id}/livestreams                                 # Start for meeting
POST /meetings/{meeting_id}/active-livestream/stop                      # Stop
POST /livestreams                                                       # Create independent: returns {ingest_server, stream_key, playback_url}
```

### Sessions & Analytics
```bash
GET  /sessions                                                          # List all
GET  /sessions/{session_id}                                             # Get details
GET  /sessions/{session_id}/participants                                # List participants
GET  /sessions/{session_id}/participants/{participant_id}               # Call stats
GET  /sessions/{session_id}/chat                                        # Download chat CSV
GET  /sessions/{session_id}/transcript                                  # Download transcript CSV
GET  /sessions/{session_id}/summary                                     # Get summary
POST /sessions/{session_id}/summary                                     # Generate summary
GET  /analytics/daywise?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD      # Day-wise analytics
GET  /analytics/livestreams/overall                                     # Livestream analytics
```

### Webhooks
```bash
GET    /webhooks                    # List all
POST   /webhooks                    # Create: {"url": "https://...", "events": ["session.started", "session.ended"]}
PATCH  /webhooks/{webhook_id}       # Update
DELETE /webhooks/{webhook_id}       # Delete
```

