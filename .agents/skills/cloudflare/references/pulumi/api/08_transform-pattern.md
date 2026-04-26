## Transform Pattern

Modify resource args before creation:

```typescript
import {Transform} from "@pulumi/pulumi";

interface BucketArgs {
    accountId: pulumi.Input<string>;
    transform?: {bucket?: Transform<cloudflare.R2BucketArgs>};
}

function createBucket(name: string, args: BucketArgs) {
    const bucketArgs: cloudflare.R2BucketArgs = {
        accountId: args.accountId,
        name: name,
        location: "auto",
    };
    const finalArgs = args.transform?.bucket?.(bucketArgs) ?? bucketArgs;
    return new cloudflare.R2Bucket(name, finalArgs);
}
```

