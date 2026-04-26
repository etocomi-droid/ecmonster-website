## Container Class API

```typescript
import { Container } from "@cloudflare/containers";

export class MyContainer extends Container {
  defaultPort = 8080;
  requiredPorts = [8080];
  sleepAfter = "30m";
  enableInternet = true;
  pingEndpoint = "/health";
  envVars = {};
  entrypoint = [];

  onStart() { /* container started */ }
  onStop() { /* container stopping */ }
  onError(error: Error) { /* container error */ }
  onActivityExpired(): boolean { /* timeout, return true to stay alive */ }
  async alarm() { /* scheduled task */ }
}
```

