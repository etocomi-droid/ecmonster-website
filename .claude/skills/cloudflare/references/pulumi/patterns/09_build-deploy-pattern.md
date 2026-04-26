## Build + Deploy Pattern

```typescript
import * as command from "@pulumi/command";
const build = new command.local.Command("build", {create: "npm run build", dir: "./worker"});
const worker = new cloudflare.WorkerScript("worker", {
    accountId, name: "my-worker",
    content: build.stdout.apply(() => fs.readFileSync("./worker/dist/index.js", "utf8")),
}, {dependsOn: [build]});
```

