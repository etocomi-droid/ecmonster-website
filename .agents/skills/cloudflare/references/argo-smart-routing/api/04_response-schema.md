## Response Schema

All Argo Smart Routing API responses follow this structure:

```typescript
interface ArgoSmartRoutingResponse {
  result: {
    id: 'smart_routing';
    value: 'on' | 'off';
    editable: boolean;
    modified_on: string; // ISO 8601 timestamp
  };
  success: boolean;
  errors: Array<{
    code: number;
    message: string;
  }>;
  messages: Array<string>;
}
```

