### Image Management

**Distribution model:** Images pre-fetched to all global locations before deployment. Ensures fast cold starts (2-3s typical).

**Rolling deploys:** Unlike Workers (instant), container deployments roll out gradually. Old versions continue running during rollout.

**Ephemeral disk:** Container disk is ephemeral and resets on each stop. Use Durable Object storage (`this.ctx.storage`) for persistence.

