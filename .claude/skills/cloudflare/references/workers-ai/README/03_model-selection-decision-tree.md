## Model Selection Decision Tree

### Text Generation (Chat/Completion)

**Quality Priority**:
- **Best quality**: `@cf/meta/llama-3.1-70b-instruct` (expensive, ~2000 neurons)
- **Balanced**: `@cf/meta/llama-3.1-8b-instruct` (good quality, ~200 neurons)
- **Fastest/cheapest**: `@cf/mistral/mistral-7b-instruct-v0.1` (~50 neurons)

**Function Calling**:
- Use `@cf/meta/llama-3.1-8b-instruct` or `@cf/meta/llama-3.1-70b-instruct` (native tool support)

**Code Generation**:
- Use `@cf/deepseek-ai/deepseek-coder-6.7b-instruct` (specialized for code)

### Embeddings (Semantic Search/RAG)

**English text**:
- **Best**: `@cf/baai/bge-large-en-v1.5` (1024 dims, highest quality)
- **Balanced**: `@cf/baai/bge-base-en-v1.5` (768 dims, good quality)
- **Fast**: `@cf/baai/bge-small-en-v1.5` (384 dims, lower quality but fast)

**Multilingual**:
- Use `@hf/sentence-transformers/paraphrase-multilingual-minilm-l12-v2`

### Image Generation

- **Stable Diffusion**: `@cf/stabilityai/stable-diffusion-xl-base-1.0` (~10,000 neurons)
- **Portraits**: `@cf/lykon/dreamshaper-8-lcm` (optimized for faces)

### Other Tasks

- **Speech-to-text**: `@cf/openai/whisper`
- **Translation**: `@cf/meta/m2m100-1.2b` (100 languages)
- **Image classification**: `@cf/microsoft/resnet-50`

