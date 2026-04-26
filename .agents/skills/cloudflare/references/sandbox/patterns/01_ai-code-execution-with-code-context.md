## AI Code Execution with Code Context

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const { code, variables } = await request.json();
    const sandbox = getSandbox(env.Sandbox, 'ai-agent');
    
    // Create context with persistent variables
    const ctx = await sandbox.createCodeContext({
      language: 'python',
      variables: variables || {}
    });
    
    // Execute with rich outputs (text, images, HTML)
    const result = await ctx.runCode(code);
    
    return Response.json({
      outputs: result.outputs,  // [{ type: 'text'|'image'|'html', content }]
      error: result.error,
      success: !result.error
    });
  }
};
```

