### "No bundler/build step" - Pulumi uploads raw code

**Problem:** Worker fails with "Cannot use import statement outside a module"  
**Cause:** Pulumi doesn't bundle Worker code - uploads exactly what you provide  
**Solution:** Build Worker BEFORE Pulumi deploy

```typescript
// WRONG: Pulumi won't bundle this
const worker = new cloudflare.WorkerScript("worker", {
    content: fs.readFileSync("./src/index.ts", "utf8"), // Raw TS file
});

// RIGHT: Build first, then deploy
import * as command from "@pulumi/command";
const build = new command.local.Command("build", {
    create: "npm run build",
    dir: "./worker",
});
const worker = new cloudflare.WorkerScript("worker", {
    content: build.stdout.apply(() => fs.readFileSync("./worker/dist/index.js", "utf8")),
}, {dependsOn: [build]});
```

