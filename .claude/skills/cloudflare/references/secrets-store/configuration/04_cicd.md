## CI/CD

### GitHub Actions

```yaml
- name: Create secret
  env:
    CLOUDFLARE_API_TOKEN: ${{ secrets.CF_TOKEN }}
  run: |
    echo "${{ secrets.API_KEY }}" | \
    npx wrangler secrets-store secret create $STORE_ID \
      --name API_KEY --scopes workers --remote

- name: Deploy
  run: npx wrangler deploy
```

### GitLab CI

```yaml
script:
  - echo "$API_KEY_VALUE" | npx wrangler secrets-store secret create $STORE_ID --name API_KEY --scopes workers --remote
  - npx wrangler deploy
```

See: [api.md](./api.md), [patterns.md](./patterns.md)
