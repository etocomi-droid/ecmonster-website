### "Body has already been used"

**Cause:** Attempting to read response body twice (bodies are streams)  
**Solution:** Clone response before reading: `response.clone()` or read once and create new Response with the text

