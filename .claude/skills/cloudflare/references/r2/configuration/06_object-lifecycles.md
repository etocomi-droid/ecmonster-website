## Object Lifecycles

```typescript
import { PutBucketLifecycleConfigurationCommand } from '@aws-sdk/client-s3';

await s3.send(new PutBucketLifecycleConfigurationCommand({
  Bucket: 'my-bucket',
  LifecycleConfiguration: {
    Rules: [
      {
        ID: 'expire-old-logs',
        Status: 'Enabled',
        Prefix: 'logs/',
        Expiration: { Days: 90 }
      },
      {
        ID: 'transition-to-ia',
        Status: 'Enabled',
        Prefix: 'archives/',
        Transitions: [{ Days: 30, StorageClass: 'STANDARD_IA' }]
      }
    ]
  }
}));
```

