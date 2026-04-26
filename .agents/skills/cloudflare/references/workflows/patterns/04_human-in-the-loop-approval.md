## Human-in-the-Loop Approval

```typescript
export class ApprovalWorkflow extends WorkflowEntrypoint<Env, Params> {
  async run(event, step) {
    await step.do('create approval', async () => await this.env.DB.prepare('INSERT INTO approvals (id, user_id, status) VALUES (?, ?, ?)').bind(event.instanceId, event.payload.userId, 'pending').run());
    try {
      const approval = await step.waitForEvent<{ approved: boolean }>('wait for approval', { event: 'approval-response', timeout: '48h' });
      if (approval.approved) { await step.do('process approval', async () => {}); } 
      else { await step.do('handle rejection', async () => {}); }
    } catch (e) {
      await step.do('auto reject', async () => await this.env.DB.prepare('UPDATE approvals SET status = ? WHERE id = ?').bind('auto-rejected', event.instanceId).run());
    }
  }
}
```

