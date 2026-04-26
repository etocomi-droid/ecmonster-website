## Workflows (Step Orchestration)

```typescript
import { WorkflowEntrypoint, WorkflowStep, WorkflowEvent } from 'cloudflare:workers';

export class MyWorkflow extends WorkflowEntrypoint {
  async run(event: WorkflowEvent<{ userId: string }>, step: WorkflowStep) {
    const user = await step.do('fetch-user', async () => 
      fetch(`/api/users/${event.payload.userId}`).then(r => r.json())
    );
    await step.sleep('wait', '1 hour');
    await step.do('notify', async () => sendEmail(user.email));
  }
}
```

Multi-step jobs with automatic retries, state persistence, resume from failure

