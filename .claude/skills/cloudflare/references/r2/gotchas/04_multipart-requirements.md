## Multipart Requirements

- All parts must be uniform size (except last part)
- Part numbers start at 1 (not 0)
- Uncompleted uploads auto-abort after 7 days
- `resumeMultipartUpload` doesn't validate uploadId existence

