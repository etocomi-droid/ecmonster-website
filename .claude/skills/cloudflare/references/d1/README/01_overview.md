## Overview

D1 is Cloudflare's managed, serverless database with:
- SQLite SQL semantics and compatibility
- Built-in disaster recovery via Time Travel (30-day point-in-time recovery)
- Horizontal scale-out architecture (10 GB per database)
- Worker and HTTP API access
- Pricing based on query and storage costs only

**Architecture Philosophy**: D1 is optimized for per-user, per-tenant, or per-entity database patterns rather than single large databases.

