## UI Kit (Minimal Code)

```tsx
// React
import { RtkMeeting } from '@cloudflare/realtimekit-react-ui';
<RtkMeeting authToken="<token>" onLeave={() => console.log('Left')} />

// Angular
@Component({ template: `<rtk-meeting [authToken]="authToken" (rtkLeave)="onLeave($event)"></rtk-meeting>` })
export class AppComponent { authToken = '<token>'; onLeave(event: unknown) {} }

// HTML/Web Components
<script type="module" src="https://cdn.jsdelivr.net/npm/@cloudflare/realtimekit-ui/dist/realtimekit-ui/realtimekit-ui.esm.js"></script>
<rtk-meeting id="meeting"></rtk-meeting>
<script>document.getElementById('meeting').authToken = '<token>';</script>
```

