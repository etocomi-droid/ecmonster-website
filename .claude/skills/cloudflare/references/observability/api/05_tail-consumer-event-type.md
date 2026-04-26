### Tail Consumer Event Type

```typescript
interface TraceItem {
  event: TraceEvent;
  logs: TraceLog[];
  exceptions: TraceException[];
  scriptName?: string;
}

interface TraceEvent {
  outcome: 'ok' | 'exception' | 'exceededCpu' | 'exceededMemory' | 'unknown';
  cpuTime: number; // microseconds
  wallTime: number; // microseconds
}

interface TraceLog {
  timestamp: number;
  level: 'log' | 'info' | 'debug' | 'warn' | 'error';
  message: any; // string or structured object
}

interface TraceException {
  name: string;
  message: string;
  timestamp: number;
}
```