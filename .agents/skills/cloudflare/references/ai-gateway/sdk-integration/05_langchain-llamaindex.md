## LangChain / LlamaIndex

```typescript
// Use OpenAI SDK pattern with custom baseURL
new ChatOpenAI({
  configuration: {
    baseURL: `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/openai`
  }
});
```

