### Container Class Properties

```typescript
import { Container } from "@cloudflare/containers";

export class MyContainer extends Container {
  // Port Configuration
  defaultPort = 8080;             // Default port for fetch() calls
  requiredPorts = [8080, 9090];   // Ports to wait for in startAndWaitForPorts()

  // Lifecycle
  sleepAfter = "30m";             // Inactivity timeout (5m, 30m, 2h, etc.)

  // Network
  enableInternet = true;          // Allow outbound internet access

  // Health Check
  pingEndpoint = "/health";       // Health check endpoint path

  // Environment
  envVars = {                     // Environment variables passed to container
    NODE_ENV: "production",
    LOG_LEVEL: "info"
  };

  // Startup
  entrypoint = ["/bin/start.sh"]; // Override image entrypoint (optional)
}
```

**Property details:**

- **`defaultPort`**: Port used when calling `container.fetch()` without explicit port. Falls back to port 33 if not set.

- **`requiredPorts`**: Array of ports that must be listening before `startAndWaitForPorts()` returns. First port becomes default if `defaultPort` not set.

- **`sleepAfter`**: Duration string (e.g., "5m", "30m", "2h"). Container stops after this period of inactivity. Timer resets on each request.

- **`enableInternet`**: Boolean. If `true`, container can make outbound HTTP/TCP requests.

- **`pingEndpoint`**: Path used for health checks. Should respond with 2xx status.

- **`envVars`**: Object of environment variables. Merged with runtime-provided vars (see below).

- **`entrypoint`**: Array of strings. Overrides container image's CMD/ENTRYPOINT.

