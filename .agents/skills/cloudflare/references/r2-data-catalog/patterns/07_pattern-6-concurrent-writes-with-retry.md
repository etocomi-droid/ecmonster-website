## Pattern 6: Concurrent Writes with Retry

```python
from pyiceberg.exceptions import CommitFailedException
import time

def append_with_retry(table, data, max_retries=3):
    for attempt in range(max_retries):
        try:
            table.append(data)
            return
        except CommitFailedException:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
```

