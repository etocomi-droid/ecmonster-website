## Distance Metric Selection

Choose based on your use case:

```
What are you building?
├─ Text/semantic search → cosine (most common)
├─ Image similarity → euclidean
├─ Recommendation system → dot-product
└─ Pre-normalized vectors → dot-product
```

| Metric | Best For | Score Interpretation |
|--------|----------|---------------------|
| `cosine` | Text embeddings, semantic similarity | Higher = closer (1.0 = identical) |
| `euclidean` | Absolute distance, spatial data | Lower = closer (0.0 = identical) |
| `dot-product` | Recommendations, normalized vectors | Higher = closer |

**Note:** Index configuration is immutable. Cannot change dimensions or metric after creation.

