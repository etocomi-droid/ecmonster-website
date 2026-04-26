## When to Use AI Search

### AI Search vs Vectorize

| Factor | AI Search | Vectorize |
|--------|-----------|-----------|
| **Management** | Fully managed | Manual embedding + indexing |
| **Use when** | Want zero-ops RAG pipeline | Need custom embeddings/control |
| **Indexing** | Automatic (6hr cycle) | Manual via API |
| **Generation** | Built-in optional | Bring your own LLM |
| **Data sources** | R2 or website | Manual insert |
| **Best for** | Docs, support, enterprise search | Custom ML pipelines, real-time |

### AI Search vs Direct Workers AI

| Factor | AI Search | Workers AI (direct) |
|--------|-----------|---------------------|
| **Context** | Automatic retrieval | Manual context building |
| **Use when** | Need RAG (search + generate) | Simple generation tasks |
| **Indexing** | Built-in | Not applicable |
| **Best for** | Knowledge bases, docs | Simple chat, transformations |

### search() vs aiSearch()

| Method | Returns | Use When |
|--------|---------|----------|
| `search()` | Search results only | Building custom UI, need raw chunks |
| `aiSearch()` | AI response + results | Need ready-to-use answer (chatbot, Q&A) |

### Real-time Updates Consideration

**AI Search is NOT ideal if:**
- Need real-time content updates (<6 hours)
- Content changes multiple times per hour
- Strict freshness requirements

**AI Search IS ideal if:**
- Content relatively stable (docs, policies, knowledge bases)
- 6-hour refresh acceptable
- Prefer zero-ops over real-time

