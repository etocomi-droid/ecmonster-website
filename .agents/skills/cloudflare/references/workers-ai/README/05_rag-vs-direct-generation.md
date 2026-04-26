## RAG vs Direct Generation

### Use RAG (Vectorize + Workers AI) When:
- Answering questions about specific documents/data
- Need factual accuracy from known corpus
- Context exceeds model's window (>4K tokens)
- Building knowledge base chat

### Use Direct Generation When:
- Creative writing, brainstorming
- General knowledge questions
- Small context fits in prompt (<4K tokens)
- Cost optimization (RAG adds embedding + vector search costs)

