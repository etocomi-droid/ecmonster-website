### "AI Gateway unavailable"

**Cause:** AI service timeout or quota exceeded  
**Solution:** Add error handling and fallbacks:
```ts
try { 
  return await this.env.AI.run(model, {prompt}); 
} catch (e) { 
  console.error("AI error:", e);
  return {error: "Unavailable"}; 
}
```

