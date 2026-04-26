## User Lifecycle

```typescript
export class UserLifecycleWorkflow extends WorkflowEntrypoint<Env, Params> {
  async run(event, step) {
    await step.do('welcome email', async () => await sendEmail(event.payload.email, 'Welcome!'));
    await step.sleep('trial period', '7 days');
    const hasConverted = await step.do('check conversion', async () => {
      const user = await this.env.DB.prepare('SELECT subscription_status FROM users WHERE id = ?').bind(event.payload.userId).first();
      return user.subscription_status === 'active';
    });
    if (!hasConverted) await step.do('trial expiration email', async () => await sendEmail(event.payload.email, 'Trial ending'));
  }
}
```

