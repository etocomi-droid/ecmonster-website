## Data Handling Issues

### Assuming Single Read Gets All Data

**Problem:** Only reading once may miss chunked data

**Solution:** Loop `reader.read()` until `done === true` (see patterns.md)

### Text Encoding Issues

**Problem:** Using wrong encoding

**Solution:** Specify encoding: `new TextDecoder('iso-8859-1').decode(data)`

