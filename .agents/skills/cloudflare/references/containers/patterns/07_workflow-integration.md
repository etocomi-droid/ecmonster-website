## Workflow Integration

```typescript
import { WorkflowEntrypoint } from "cloudflare:workers";

export class ProcessingWorkflow extends WorkflowEntrypoint {
  async run(event, step) {
    const container = this.env.PROCESSOR.getByName(event.payload.jobId);
    
    await step.do("start", async () => {
      await container.startAndWaitForPorts();
    });
    
    const result = await step.do("process", async () => {
      return container.fetch("/process", {
        method: "POST",
        body: JSON.stringify(event.payload.data)
      }).then(r => r.json());
    });
    
    return result;
  }
}
```

**Use:** Orchestrating multi-step container operations, durable execution.

