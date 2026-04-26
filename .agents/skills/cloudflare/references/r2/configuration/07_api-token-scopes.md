## API Token Scopes

When creating R2 tokens, set minimal permissions:

| Permission | Use Case |
|------------|----------|
| Object Read | Public serving, downloads |
| Object Write | Uploads only |
| Object Read & Write | Full object operations |
| Admin Read & Write | Bucket management, CORS, lifecycles |

**Best practice:** Separate tokens for Workers (read/write) vs admin tasks (CORS, lifecycles).

