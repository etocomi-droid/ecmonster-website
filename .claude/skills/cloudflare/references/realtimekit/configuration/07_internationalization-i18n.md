## Internationalization (i18n)

### Custom Language Strings
```typescript
import { useLanguage } from '@cloudflare/realtimekit-ui';

const customLanguage = {
  'join': 'Entrar',
  'leave': 'Salir',
  'mute': 'Silenciar',
  'unmute': 'Activar audio',
  'turn_on_camera': 'Encender cámara',
  'turn_off_camera': 'Apagar cámara',
  'share_screen': 'Compartir pantalla',
  'stop_sharing': 'Dejar de compartir'
};

const t = useLanguage(customLanguage);

// React usage
<RtkMeeting authToken={token} t={t} onLeave={() => {}} />
```

### Supported Locales
Default locales available: `en`, `es`, `fr`, `de`, `pt`, `ja`, `zh`

```typescript
import { setLocale } from '@cloudflare/realtimekit-ui';
setLocale('es');  // Switch to Spanish
```

