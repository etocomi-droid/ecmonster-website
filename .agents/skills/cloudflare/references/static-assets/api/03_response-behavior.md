## Response Behavior

### Content-Type Inference

Automatically set based on file extension:

| Extension | Content-Type |
|-----------|--------------|
| `.html` | `text/html; charset=utf-8` |
| `.css` | `text/css` |
| `.js` | `application/javascript` |
| `.json` | `application/json` |
| `.png` | `image/png` |
| `.jpg`, `.jpeg` | `image/jpeg` |
| `.svg` | `image/svg+xml` |
| `.woff2` | `font/woff2` |

### Default Headers

Responses include:

```
Content-Type: <inferred>
ETag: "<hash>"
Cache-Control: public, max-age=3600
Content-Encoding: br  (if supported and beneficial)
```

**Cache-Control defaults:**

- 1 hour (`max-age=3600`) for most assets
- Override via Worker response transformation (see patterns.md:27-35)

### Compression

Automatic compression based on `Accept-Encoding`:

- **Brotli** (`br`): Preferred, best compression
- **Gzip** (`gzip`): Fallback
- **None**: If client doesn't support or asset too small

### ETag Generation

ETags are content-based hashes:

```
ETag: "a3b2c1d4e5f6..."
```

Used for conditional requests (`If-None-Match`). Returns `304 Not Modified` if match.

