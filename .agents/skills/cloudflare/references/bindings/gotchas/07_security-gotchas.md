## Security Gotchas

**❌ Secrets in logs:** `console.log('Key:', env.API_KEY)` - visible in dashboard  
**✅** `console.log('Key:', env.API_KEY ? '***' : 'missing')`

**❌ Exposing env:** `return Response.json(env)` - exposes all bindings  
**✅** Never return env object in responses

