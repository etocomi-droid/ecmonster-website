## Type Safety

```typescript
// Error response type
interface StreamError {
  success: false;
  errors: Array<{
    code: number;
    message: string;
  }>;
}

// Handle errors
async function uploadWithErrorHandling(url: string, file: File) {
  const formData = new FormData();
  formData.append('file', file);
  const response = await fetch(url, { method: 'POST', body: formData });
  const result = await response.json();
  
  if (!result.success) {
    throw new Error(result.errors[0]?.message || 'Upload failed');
  }
  return result;
}
```

