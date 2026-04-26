## Error Handling

- **Missing keys:** Return `null` (not an error)
- **Rate limit (429):** Retry with exponential backoff (see gotchas.md)
- **Response too large (413):** Values >25MB fail with 413 error

See [gotchas.md](./gotchas.md) for detailed error patterns and solutions.
