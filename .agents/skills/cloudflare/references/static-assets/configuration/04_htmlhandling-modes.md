### html_handling Modes

Controls trailing slash behavior for HTML files:

| Mode | `/page` | `/page/` | Use Case |
|------|---------|----------|----------|
| `"auto-trailing-slash"` | Redirect to `/page/` if `/page/index.html` exists | Serve `/page/index.html` | Default, SEO-friendly |
| `"force-trailing-slash"` | Always redirect to `/page/` | Serve if exists | Consistent trailing slashes |
| `"drop-trailing-slash"` | Serve if exists | Redirect to `/page` | Cleaner URLs |
| `"none"` | No modification | No modification | Custom routing logic |

**Default:** `"auto-trailing-slash"`

