## TraceItem Type

```typescript
interface TraceItem {
  scriptName: string;           // Producer Worker name
  eventTimestamp: number;        // Epoch milliseconds
  outcome: 'ok' | 'exception' | 'exceededCpu' | 'exceededMemory' 
         | 'canceled' | 'scriptNotFound' | 'responseStreamDisconnected' | 'unknown';
  
  event?: {
    request?: {
      url: string;               // Redacted by default
      method: string;
      headers: Record<string, string>;  // Sensitive headers redacted
      cf?: IncomingRequestCfProperties;
      getUnredacted(): TraceRequest;    // Bypass redaction (use carefully)
    };
    response?: {
      status: number;
    };
  };
  
  logs: Array<{
    timestamp: number;           // Epoch milliseconds
    level: 'debug' | 'info' | 'log' | 'warn' | 'error';
    message: unknown[];          // Args passed to console function
  }>;
  
  exceptions: Array<{
    timestamp: number;           // Epoch milliseconds
    name: string;                // Error type (Error, TypeError, etc.)
    message: string;             // Error description
  }>;
  
  diagnosticsChannelEvents: Array<{
    channel: string;
    message: unknown;
    timestamp: number;           // Epoch milliseconds
  }>;
}
```

**Note:** Official SDK uses `TraceItem`, not `TailItem`. Use `@cloudflare/workers-types` for accurate types.

