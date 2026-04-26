## Client Setup

### curl

```bash
curl -s https://api.cloudflare.com/client/v4/graphql \
  -H "Authorization: Bearer $CF_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "query": "query($zoneTag: string!, $start: Time!, $end: Time!) { viewer { zones(filter: {zoneTag: $zoneTag}) { httpRequestsAdaptiveGroups(filter: {datetime_gt: $start, datetime_lt: $end}, limit: 10, orderBy: [datetimeFiveMinutes_DESC]) { count dimensions { datetimeFiveMinutes } } } } }",
    "variables": { "zoneTag": "ZONE_ID", "start": "2025-01-01T00:00:00Z", "end": "2025-01-02T00:00:00Z" }
  }' | jq .
```

### TypeScript / JavaScript

```typescript
const GRAPHQL_ENDPOINT = "https://api.cloudflare.com/client/v4/graphql";

async function queryGraphQL<T>(query: string, variables: Record<string, unknown> = {}): Promise<T> {
  const response = await fetch(GRAPHQL_ENDPOINT, {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.CF_API_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify({ query, variables }),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  const json = await response.json() as { data: T | null; errors?: { message: string }[] };
  if (json.errors?.length) throw new Error(json.errors.map((e) => e.message).join("; "));
  return json.data!;
}
```

### Python

```python
import requests, os

def query_graphql(query: str, variables: dict = None) -> dict:
    r = requests.post("https://api.cloudflare.com/client/v4/graphql",
        headers={"Authorization": f"Bearer {os.environ['CF_API_TOKEN']}", "Content-Type": "application/json"},
        json={"query": query, "variables": variables or {}})
    r.raise_for_status()
    result = r.json()
    if result.get("errors"):
        raise Exception("; ".join(e["message"] for e in result["errors"]))
    return result["data"]
```

### From a Cloudflare Worker

Store the API token as a secret (`CF_API_TOKEN`). Use standard `fetch` to POST to `https://api.cloudflare.com/client/v4/graphql` with the same JSON body format as above. Always check `response.errors` — GraphQL returns 200 even on query failures.

