## Miniflare Limitations

**Not supported:**
- Analytics Engine (use mocks)
- Cloudflare Images/Stream
- Browser Rendering API
- Tail Workers
- Workers for Platforms (partial support)

**Behavior differences from production:**
- Runs workerd locally, not Cloudflare edge
- Storage is local (filesystem/memory), not distributed
- `Request.cf` is cached/mocked, not real edge data
- Performance differs from edge
- Caching implementation may vary slightly

