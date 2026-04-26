## Detecting Smart Placement in Code

**Note:** `cf-placement` header is a beta feature and may change or be removed.

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const placementHeader = request.headers.get('cf-placement');
    
    if (placementHeader?.startsWith('remote-')) {
      const location = placementHeader.split('-')[1];
      console.log(`Smart Placement routed to ${location}`);
    } else if (placementHeader?.startsWith('local-')) {
      const location = placementHeader.split('-')[1];
      console.log(`Running at edge location ${location}`);
    }
    
    return new Response('OK');
  }
} satisfies ExportedHandler<Env>;
```

