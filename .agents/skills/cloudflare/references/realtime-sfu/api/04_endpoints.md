## Endpoints

### Create Session
```http
POST /v1/apps/{appId}/sessions/new
→ {sessionId, sessionDescription}
```

### Add Track (Publish)
```http
POST /v1/apps/{appId}/sessions/{sessionId}/tracks/new
Body: {
  sessionDescription: {sdp, type: "offer"},
  tracks: [{location: "local", trackName: "my-video"}]
}
→ {sessionDescription, tracks: [{trackName}]}
```

### Add Track (Subscribe)
```http
POST /v1/apps/{appId}/sessions/{sessionId}/tracks/new
Body: {
  tracks: [{
    location: "remote",
    trackName: "remote-track-id",
    sessionId: "other-session-id"
  }]
}
→ {sessionDescription} (server offer)
```

### Renegotiate
```http
PUT /v1/apps/{appId}/sessions/{sessionId}/renegotiate
Body: {sessionDescription: {sdp, type: "answer"}}
```

### Close Tracks
```http
PUT /v1/apps/{appId}/sessions/{sessionId}/tracks/close
Body: {tracks: [{trackName}]}
→ {requiresImmediateRenegotiation: boolean}
```

### Get Session
```http
GET /v1/apps/{appId}/sessions/{sessionId}
→ {sessionId, tracks: TrackMetadata[]}
```

