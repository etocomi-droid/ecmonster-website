## Overview

**AI Search** is a managed RAG (Retrieval-Augmented Generation) pipeline that combines:
- Automatic semantic indexing of your content
- Vector similarity search
- Built-in LLM generation

**Key value propositions:**
- **Zero vector management** - No manual embedding, indexing, or storage
- **Auto-indexing** - Content automatically re-indexed every 6 hours
- **Built-in generation** - Optional AI response generation from retrieved context
- **Multi-source** - Index from R2 buckets or website crawls

**Data source options:**
- **R2 bucket** - Index files from Cloudflare R2 (supports MD, TXT, HTML, PDF, DOC, CSV, JSON)
- **Website** - Crawl and index website content (requires Cloudflare-hosted domain)

**Indexing lifecycle:**
- Automatic 6-hour refresh cycle
- Manual "Force Sync" available (30s rate limit)
- Not designed for real-time updates

