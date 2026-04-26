## Interactive Flow

When run without flags, C3 prompts in this order:

1. **Project name** - Directory to create (defaults to current dir with `.`)
2. **Application type** - `hello-world`, `web-app`, `demo`, `pre-existing`, `remote-template`
3. **Platform** - `workers` (default) or `pages` (for web apps only)
4. **Framework** - If web-app: `next`, `remix`, `astro`, `react-router`, `solid`, `svelte`, etc.
5. **TypeScript** - `yes` (recommended) or `no`
6. **Git** - Initialize repository? `yes` or `no`
7. **Deploy** - Deploy now? `yes` or `no` (requires `wrangler login`)

