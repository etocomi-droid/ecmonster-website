## Callback Signatures

```typescript
type TurnstileCallback = (token: string) => void;
type ErrorCallback = (errorCode: string) => void;
type TimeoutCallback = () => void;
type ExpiredCallback = () => void;
type BeforeInteractiveCallback = () => void;
type AfterInteractiveCallback = () => void;
type UnsupportedCallback = () => void;
```

