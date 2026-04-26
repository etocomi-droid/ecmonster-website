## Wrangler CLI

```bash
npm create cloudflare@latest my-workflow -- --template "cloudflare/workflows-starter"
npx wrangler deploy
npx wrangler workflows list
npx wrangler workflows trigger my-workflow '{"userId":"user123"}'
npx wrangler workflows instances list my-workflow
npx wrangler workflows instances describe my-workflow instance-id
npx wrangler workflows instances pause/resume/terminate my-workflow instance-id
```

