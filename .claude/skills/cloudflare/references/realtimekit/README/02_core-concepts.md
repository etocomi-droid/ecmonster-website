## Core Concepts

- **App**: Workspace grouping meetings, participants, presets, recordings. Use separate Apps for staging/production
- **Meeting**: Re-usable virtual room. Each join creates new **Session**
- **Session**: Live meeting instance. Created on first join, ends after last leave
- **Participant**: User added via REST API. Returns `authToken` for client SDK. **Do not reuse tokens**
- **Preset**: Reusable permission/UI template (permissions, meeting type, theme). Applied at participant creation
- **Peer ID** (`id`): Unique per session, changes on rejoin
- **Participant ID** (`userId`): Persistent across sessions

