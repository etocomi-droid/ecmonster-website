## External API Integration

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const apiUrl = 'https://api.partner.com';
    const headers = { 'Authorization': `Bearer ${env.API_KEY}` };
    
    const [profile, transactions] = await Promise.all([
      fetch(`${apiUrl}/profile`, { headers }),
      fetch(`${apiUrl}/transactions`, { headers })
    ]);
    
    return Response.json({ 
      profile: await profile.json(), 
      transactions: await transactions.json()
    });
  }
};
```

