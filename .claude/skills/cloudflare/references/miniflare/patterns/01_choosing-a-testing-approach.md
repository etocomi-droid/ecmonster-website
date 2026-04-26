## Choosing a Testing Approach

| Approach | Use Case | Speed | Setup | Runtime |
|----------|----------|-------|-------|---------|
| **getPlatformProxy** | Unit tests, logic testing | Fast | Low | Miniflare |
| **Miniflare API** | Integration tests, full control | Medium | Medium | Miniflare |
| **vitest-pool-workers** | Vitest runner integration | Medium | Medium | workerd |

**Quick guide:**
- Unit tests → getPlatformProxy
- Integration tests → Miniflare API
- Vitest workflows → vitest-pool-workers

