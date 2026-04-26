## Client SDK Configuration

### React UI Kit
```tsx
import { RtkMeeting } from '@cloudflare/realtimekit-react-ui';
<RtkMeeting authToken="<token>" onLeave={() => {}} />
```

### Angular UI Kit
```typescript
@Component({ template: `<rtk-meeting [authToken]="authToken" (rtkLeave)="onLeave($event)"></rtk-meeting>` })
export class AppComponent { authToken = '<token>'; onLeave() {} }
```

### Web Components
```html
<script type="module" src="https://cdn.jsdelivr.net/npm/@cloudflare/realtimekit-ui/dist/realtimekit-ui/realtimekit-ui.esm.js"></script>
<rtk-meeting id="meeting"></rtk-meeting>
<script>
  document.getElementById('meeting').authToken = '<token>';
</script>
```

### Core SDK Configuration
```typescript
import RealtimeKitClient from '@cloudflare/realtimekit';

const meeting = new RealtimeKitClient({
  authToken: '<token>',
  video: true, audio: true, autoSwitchAudioDevice: true,
  mediaConfiguration: {
    video: { width: { ideal: 1280 }, height: { ideal: 720 }, frameRate: { ideal: 30 } },
    audio: { echoCancellation: true, noiseSuppression: true, autoGainControl: true },
    screenshare: { width: { max: 1920 }, height: { max: 1080 }, frameRate: { ideal: 15 } }
  }
});
await meeting.join();
```

