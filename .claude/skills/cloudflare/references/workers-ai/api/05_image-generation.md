## Image Generation

```typescript
const image = await env.AI.run('@cf/stabilityai/stable-diffusion-xl-base-1.0', {
  prompt: 'Mountain sunset',
  num_steps: 20,   // 1-20
  guidance: 7.5    // 1-20
});
return new Response(image, { headers: { 'Content-Type': 'image/png' } });
```

