## Platform Decision Tree

```
What are you building?

├─ API / WebSocket / Cron / Email handler
│   └─ Workers (default) - no --platform flag needed
│       npm create cloudflare@latest my-api -- --type=hello-world

├─ Static site / SSG / Documentation
│   └─ Pages - requires --platform=pages
│       npm create cloudflare@latest my-site -- --type=web-app --framework=astro --platform=pages

├─ Full-stack app (Next.js/Remix/SvelteKit)
│   ├─ Need Durable Objects, Queues, or Workers-only features?
│   │   └─ Workers (default)
│   └─ Otherwise use Pages for git integration and branch previews
│       └─ Add --platform=pages

└─ Convert existing project
    └─ npm create cloudflare@latest . -- --type=pre-existing --existing-script=./src/worker.ts
```

**Critical:** Pages projects require `--platform=pages` flag. Without it, C3 defaults to Workers.

