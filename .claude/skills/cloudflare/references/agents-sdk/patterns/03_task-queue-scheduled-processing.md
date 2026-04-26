## Task Queue & Scheduled Processing

```ts
export class TaskAgent extends Agent<Env> {
  onStart() { 
    this.schedule("*/5 * * * *", "processQueue", {}); // Every 5 min
    this.schedule("0 0 * * *", "dailyCleanup", {}); // Daily
  }
  
  async onRequest(req: Request) {
    await this.queue("processVideo", { videoId: (await req.json()).videoId });
    return Response.json({ queued: true });
  }
  
  async processQueue() {
    const tasks = await this.dequeue(10);
    for (const task of tasks) {
      if (task.name === "processVideo") await this.processVideo(task.data.videoId);
    }
  }
  
  async dailyCleanup() {
    this.sql`DELETE FROM logs WHERE created_at < ${Date.now() - 86400000}`;
  }
}
```

