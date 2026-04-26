## Debugging with chrome://webrtc-internals

1. Open `chrome://webrtc-internals` in Chrome/Edge
2. Find your PeerConnection in the list
3. Check **Stats graphs** for packet loss, jitter, bandwidth
4. Check **ICE candidate pairs**: Look for `succeeded` state, relay vs host candidates
5. Check **getStats**: Raw metrics for inbound/outbound RTP
6. Look for errors in **Event log**: `iceConnectionState`, `connectionState` changes
7. Export data with "Download the PeerConnection updates and stats data" button
8. Common issues visible here: ICE failures, high packet loss, bitrate drops

