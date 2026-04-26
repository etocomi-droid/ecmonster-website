### 4. Pulumi
**Best for**: Multi-cloud IaC, TypeScript/Python/Go workflows

```typescript
import * as cloudflare from "@pulumi/cloudflare";
import * as fs from "fs";

// Create snippet
const securitySnippet = new cloudflare.Snippet("security-headers", {
  zoneId: zoneId,
  name: "security_headers",
  mainModule: "security_headers.js",
  files: [{
    name: "security_headers.js",
    content: fs.readFileSync("./snippets/security_headers.js", "utf8"),
  }],
});

// Create snippet rule
const snippetRule = new cloudflare.SnippetRules("security-rules", {
  zoneId: zoneId,
  rules: [{
    description: "Apply security headers",
    enabled: true,
    expression: "true",
    snippetName: securitySnippet.name,
  }],
});
```

