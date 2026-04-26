## RPC Methods (@callable)

```ts
import { Agent, callable } from "agents";

export class MyAgent extends Agent<Env> {
  @callable()
  async processTask(input: {text: string}): Promise<{result: string}> {
    return { result: await this.env.AI.run("@cf/meta/llama-3.1-8b-instruct", {prompt: input.text}) };
  }
}
// Client: const result = await agent.processTask({ text: "Hello" });
// Must return JSON-serializable values
```

