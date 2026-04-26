## Storage Class Pitfalls

- InfrequentAccess: 30-day minimum billing (even if deleted early)
- Can't transition IA → Standard via lifecycle (use S3 CopyObject)
- Retrieval fees apply for IA reads

