## Common Errors

### "ERR_NON_VIDEO"

**Cause:** Uploaded file is not a valid video format
**Solution:** Ensure file is in supported format (MP4, MKV, MOV, AVI, FLV, MPEG-2 TS/PS, MXF, LXF, GXF, 3GP, WebM, MPG, QuickTime)

### "ERR_DURATION_EXCEED_CONSTRAINT"

**Cause:** Video duration exceeds `maxDurationSeconds` constraint
**Solution:** Increase `maxDurationSeconds` in direct upload config or trim video before upload

### "ERR_FETCH_ORIGIN_ERROR"

**Cause:** Failed to download video from URL (upload from URL)
**Solution:** Ensure URL is publicly accessible, uses HTTPS, and video file is available

### "ERR_MALFORMED_VIDEO"

**Cause:** Video file is corrupted or improperly encoded
**Solution:** Re-encode video using FFmpeg or check source file integrity

### "ERR_DURATION_TOO_SHORT"

**Cause:** Video must be at least 0.1 seconds long
**Solution:** Ensure video has valid duration (not a single frame)

