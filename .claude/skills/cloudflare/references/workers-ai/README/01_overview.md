## Overview

Workers AI provides:
- 50+ pre-trained models (LLMs, embeddings, image generation, speech-to-text, translation)
- Native Workers binding (no external API calls)
- Pay-per-use pricing (neurons consumed per inference)
- OpenAI-compatible REST API
- Streaming support for text generation
- Function calling with compatible models

**Architecture**: Inference runs on Cloudflare's GPU network. Models load on first request (cold start 1-3s), subsequent requests are faster.

