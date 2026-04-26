## Core SDK Patterns

### Basic Setup
```typescript
import RealtimeKitClient from '@cloudflare/realtimekit';

const meeting = new RealtimeKitClient({ authToken, video: true, audio: true });
meeting.self.on('roomJoined', () => console.log('Joined:', meeting.meta.meetingTitle));
meeting.participants.joined.on('participantJoined', (p) => console.log(`${p.name} joined`));
await meeting.join();
```

### Video Grid & Device Selection
```typescript
// Video grid
function VideoGrid({ meeting }) {
  const [participants, setParticipants] = useState([]);
  useEffect(() => {
    const update = () => setParticipants(meeting.participants.joined.toArray());
    meeting.participants.joined.on('participantJoined', update);
    meeting.participants.joined.on('participantLeft', update);
    update();
    return () => { meeting.participants.joined.off('participantJoined', update); meeting.participants.joined.off('participantLeft', update); };
  }, [meeting]);
  return <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))' }}>
    {participants.map(p => <VideoTile key={p.id} participant={p} />)}
  </div>;
}

function VideoTile({ participant }) {
  const videoRef = useRef<HTMLVideoElement>(null);
  useEffect(() => {
    if (videoRef.current && participant.videoTrack) videoRef.current.srcObject = new MediaStream([participant.videoTrack]);
  }, [participant.videoTrack]);
  return <div><video ref={videoRef} autoPlay playsInline muted /><div>{participant.name}</div></div>;
}

// Device selection
const devices = await meeting.self.getAllDevices();
const switchCamera = (deviceId: string) => {
  const device = devices.find(d => d.deviceId === deviceId);
  if (device) await meeting.self.setDevice(device);
};
```

