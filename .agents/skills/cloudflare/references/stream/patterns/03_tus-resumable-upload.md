## TUS Resumable Upload

For large files (>500MB). `npm install tus-js-client`

```typescript
import * as tus from 'tus-js-client';

async function uploadWithTUS(file: File, uploadURL: string, onProgress?: (pct: number) => void) {
  return new Promise<string>((resolve, reject) => {
    const upload = new tus.Upload(file, {
      endpoint: uploadURL,
      retryDelays: [0, 3000, 5000, 10000, 20000],
      chunkSize: 50 * 1024 * 1024,
      metadata: { filename: file.name, filetype: file.type },
      onError: reject,
      onProgress: (up, total) => onProgress?.((up / total) * 100),
      onSuccess: () => resolve(upload.url?.split('/').pop() || '')
    });
    upload.start();
  });
}
```

