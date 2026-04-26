## Full-Stack Upload Flow

**Backend API (Workers/Pages)**
```typescript
import Cloudflare from 'cloudflare';

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const { videoName } = await request.json();
    const client = new Cloudflare({ apiToken: env.CF_API_TOKEN });
    const { uploadURL, uid } = await client.stream.directUpload.create({
      account_id: env.CF_ACCOUNT_ID,
      maxDurationSeconds: 3600,
      requireSignedURLs: true,
      meta: { name: videoName }
    });
    return Response.json({ uploadURL, uid });
  }
};
```

**Frontend component**
```tsx
import { useState } from 'react';

export function VideoUploader() {
  const [uploading, setUploading] = useState(false);
  const [progress, setProgress] = useState(0);
  
  async function handleUpload(file: File) {
    setUploading(true);
    const { uploadURL, uid } = await fetch('/api/upload-url', {
      method: 'POST',
      body: JSON.stringify({ videoName: file.name })
    }).then(r => r.json());
    
    const xhr = new XMLHttpRequest();
    xhr.upload.onprogress = (e) => setProgress((e.loaded / e.total) * 100);
    xhr.onload = () => { setUploading(false); window.location.href = `/videos/${uid}`; };
    xhr.open('POST', uploadURL);
    const formData = new FormData();
    formData.append('file', file);
    xhr.send(formData);
  }
  
  return (
    <div>
      <input type="file" accept="video/*" onChange={(e) => e.target.files?.[0] && handleUpload(e.target.files[0])} disabled={uploading} />
      {uploading && <progress value={progress} max={100} />}
    </div>
  );
}
```

