## Quick Start

### 1. Create App & Meeting (Backend)

```bash
# Create app
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<account_id>/realtime/kit/apps' \
  -H 'Authorization: Bearer <api_token>' \
  -d '{"name": "My RealtimeKit App"}'

# Create meeting
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<account_id>/realtime/kit/<app_id>/meetings' \
  -H 'Authorization: Bearer <api_token>' \
  -d '{"title": "Team Standup"}'

# Add participant
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<account_id>/realtime/kit/<app_id>/meetings/<meeting_id>/participants' \
  -H 'Authorization: Bearer <api_token>' \
  -d '{"name": "Alice", "preset_name": "host"}'
# Returns: { authToken }
```

### 2. Client Integration

**React**:
```tsx
import { RtkMeeting } from '@cloudflare/realtimekit-react-ui';

function App() {
  return <RtkMeeting authToken="<participant_auth_token>" onLeave={() => {}} />;
}
```

**Core SDK**:
```typescript
import RealtimeKitClient from '@cloudflare/realtimekit';

const meeting = new RealtimeKitClient({ authToken: '<token>', video: true, audio: true });
await meeting.join();
```

