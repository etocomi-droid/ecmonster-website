## Performance Issues

### Upload is slow
- **Cause**: Large file size or network constraints
- **Solution**: Use TUS resumable upload, compress video before upload, check bandwidth

### Playback buffering
- **Cause**: Network congestion or low bandwidth
- **Solution**: Use ABR (adaptive bitrate) with HLS/DASH, reduce max bitrate

### High processing time
- **Cause**: Complex video codec, high resolution
- **Solution**: Pre-encode with H.264 (most efficient), reduce resolution

