## Local Secrets (.dev.vars)

**Local dev only** - NOT deployed:

```bash
# .dev.vars (add to .gitignore)
SECRET_KEY="my-secret-value"
```

Accessed via `ctx.env.SECRET_KEY`. Set production secrets:
```bash
echo "value" | npx wrangler pages secret put SECRET_KEY --project-name=my-app
```

