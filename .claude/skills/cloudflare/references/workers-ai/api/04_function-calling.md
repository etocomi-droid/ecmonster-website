## Function Calling

```typescript
const tools = [{
  type: 'function',
  function: {
    name: 'getWeather',
    description: 'Get weather for location',
    parameters: {
      type: 'object',
      properties: { location: { type: 'string' } },
      required: ['location']
    }
  }
}];

const response = await env.AI.run(model, { messages, tools });
if (response.tool_calls) {
  const args = JSON.parse(response.tool_calls[0].function.arguments);
  // Execute function, send result back
}
```

