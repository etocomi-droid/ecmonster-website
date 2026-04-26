## Core Concepts

### Video Upload Methods
1. **API Upload (TUS protocol)**: Direct server upload
2. **Upload from URL**: Import from external source
3. **Direct Creator Uploads**: User-generated content (recommended)

### Playback Options
1. **Stream Player (iframe)**: Built-in, optimized player
2. **Custom Player (HLS/DASH)**: Video.js, HLS.js integration
3. **Thumbnails**: Static or animated previews

### Access Control
- **Public**: No restrictions
- **requireSignedURLs**: Token-based access
- **allowedOrigins**: Domain restrictions
- **Access Rules**: Geo/IP restrictions in tokens

### Live Streaming
- RTMPS/SRT ingest from OBS, FFmpeg
- Automatic recording to on-demand
- Simulcast to YouTube, Twitch, etc.
- WebRTC support for browser streaming

