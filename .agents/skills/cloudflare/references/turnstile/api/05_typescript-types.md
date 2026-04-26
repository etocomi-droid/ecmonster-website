## TypeScript Types

```typescript
interface TurnstileOptions {
  sitekey: string;
  action?: string;
  cData?: string;
  callback?: (token: string) => void;
  'error-callback'?: (errorCode: string) => void;
  'expired-callback'?: () => void;
  'timeout-callback'?: () => void;
  'before-interactive-callback'?: () => void;
  'after-interactive-callback'?: () => void;
  'unsupported-callback'?: () => void;
  theme?: 'light' | 'dark' | 'auto';
  size?: 'normal' | 'compact' | 'flexible';
  tabindex?: number;
  'response-field'?: boolean;
  'response-field-name'?: string;
  retry?: 'auto' | 'never';
  'retry-interval'?: number;
  language?: string;
  execution?: 'render' | 'execute';
  appearance?: 'always' | 'execute' | 'interaction-only';
  'refresh-expired'?: 'auto' | 'manual' | 'never';
}

interface Turnstile {
  render(container: string | HTMLElement, options: TurnstileOptions): string;
  reset(widgetId: string): void;
  remove(widgetId: string): void;
  getResponse(widgetId: string): string | undefined;
  isExpired(widgetId: string): boolean;
  execute(container?: string | HTMLElement, options?: TurnstileOptions): void;
}

declare global {
  interface Window {
    turnstile: Turnstile;
    onloadTurnstileCallback?: () => void;
  }
}
```

