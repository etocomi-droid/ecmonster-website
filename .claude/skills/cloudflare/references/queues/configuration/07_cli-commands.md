## CLI Commands

```bash
# Consumer management
wrangler queues consumer add my-queue my-worker --batch-size=50 --max-retries=5
wrangler queues consumer http add my-queue
wrangler queues consumer worker remove my-queue my-worker
wrangler queues consumer http remove my-queue

# Queue operations
wrangler queues list
wrangler queues pause my-queue
wrangler queues resume my-queue
wrangler queues purge my-queue
wrangler queues delete my-queue
```
