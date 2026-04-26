## Workflow Integration

```typescript
import { WorkflowEntrypoint } from "cloudflare:workers";

export class DataProcessingWorkflow extends WorkflowEntrypoint {
  async run(event, step) {
    const data = await step.do("fetch-data", () => fetchLargeDataset());
    const processed = await step.do("process-data", () => processDataset(data));
    await step.do("store-results", () => storeResults(processed));
  }
}

export default {
  async scheduled(controller, env, ctx) {
    const instance = await env.MY_WORKFLOW.create({
      params: { scheduledTime: controller.scheduledTime, cron: controller.cron },
    });
    console.log(`Started workflow: ${instance.id}`);
  },
};
```

