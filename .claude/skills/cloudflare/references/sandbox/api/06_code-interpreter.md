## Code Interpreter

```typescript
// Create context with variables
const ctx = await sandbox.createCodeContext({
  language: 'python',
  variables: {
    data: [1, 2, 3, 4, 5],
    config: { verbose: true }
  }
});

// Execute code with rich outputs
const result = await ctx.runCode(`
import matplotlib.pyplot as plt
plt.plot(data, [x**2 for x in data])
plt.savefig('plot.png')
print(f"Processed {len(data)} points")
`);
// Returns: { outputs: [{ type: 'text'|'image'|'html', content }], error }

// Context persists variables across runs
const result2 = await ctx.runCode('print(data[0])');  // Still has 'data'
```

