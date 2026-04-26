## TypeScript Interfaces

```typescript
interface R2Bucket {
  head(key: string): Promise<R2Object | null>;
  get(key: string, options?: R2GetOptions): Promise<R2ObjectBody | null>;
  put(key: string, value: ReadableStream | ArrayBuffer | string | Blob, options?: R2PutOptions): Promise<R2Object | null>;
  delete(keys: string | string[]): Promise<void>;
  list(options?: R2ListOptions): Promise<R2Objects>;
  createMultipartUpload(key: string, options?: R2MultipartOptions): Promise<R2MultipartUpload>;
  resumeMultipartUpload(key: string, uploadId: string): R2MultipartUpload;
}

interface R2Object {
  key: string; version: string; size: number;
  etag: string; httpEtag: string; // httpEtag is quoted, use for headers
  uploaded: Date; httpMetadata?: R2HTTPMetadata;
  customMetadata?: Record<string, string>;
  storageClass: 'Standard' | 'InfrequentAccess';
  checksums: R2Checksums;
  writeHttpMetadata(headers: Headers): void;
}

interface R2ObjectBody extends R2Object {
  body: ReadableStream; bodyUsed: boolean;
  arrayBuffer(): Promise<ArrayBuffer>; text(): Promise<string>;
  json<T>(): Promise<T>; blob(): Promise<Blob>;
}

interface R2HTTPMetadata {
  contentType?: string; contentDisposition?: string;
  contentEncoding?: string; contentLanguage?: string;
  cacheControl?: string; cacheExpiry?: Date;
}

interface R2PutOptions {
  httpMetadata?: R2HTTPMetadata | Headers;
  customMetadata?: Record<string, string>;
  sha256?: ArrayBuffer | string; // Only ONE checksum allowed
  storageClass?: 'Standard' | 'InfrequentAccess';
  ssecKey?: ArrayBuffer;
}

interface R2GetOptions {
  onlyIf?: R2Conditional | Headers;
  range?: R2Range | Headers;
  ssecKey?: ArrayBuffer;
}

interface R2ListOptions {
  limit?: number; prefix?: string; cursor?: string; delimiter?: string;
  startAfter?: string; include?: ('httpMetadata' | 'customMetadata')[];
}

interface R2Objects {
  objects: R2Object[]; truncated: boolean;
  cursor?: string; delimitedPrefixes: string[];
}

interface R2Conditional {
  etagMatches?: string; etagDoesNotMatch?: string;
  uploadedBefore?: Date; uploadedAfter?: Date;
}

interface R2Range { offset?: number; length?: number; suffix?: number; }

interface R2Checksums {
  md5?: ArrayBuffer; sha1?: ArrayBuffer; sha256?: ArrayBuffer;
  sha384?: ArrayBuffer; sha512?: ArrayBuffer;
}

interface R2MultipartUpload {
  key: string;
  uploadId: string;
  uploadPart(partNumber: number, value: ReadableStream | ArrayBuffer | string | Blob): Promise<R2UploadedPart>;
  abort(): Promise<void>;
  complete(uploadedParts: R2UploadedPart[]): Promise<R2Object>;
}

interface R2UploadedPart {
  partNumber: number;
  etag: string;
}
```

