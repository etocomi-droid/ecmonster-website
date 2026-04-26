## Model-Specific

### Function calling
Only `@cf/meta/llama-3.1-*` and `mistral-7b-instruct-v0.2` support tools.

### Empty response
Check context limits (2K-8K tokens). Validate input structure.

### Inconsistent responses
Set `temperature: 0` for deterministic outputs.

### Cold start latency
First request: 1-3s. Use AI Gateway caching for frequent prompts.

