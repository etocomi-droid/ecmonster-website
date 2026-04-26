### "setState() not syncing"

**Cause:** Mutating state directly or not calling `setState()` after modifications  
**Solution:** Always use `setState()` with immutable updates:
```ts
// ❌ this.state.count++
// ✅ this.setState({...this.state, count: this.state.count + 1})
```

