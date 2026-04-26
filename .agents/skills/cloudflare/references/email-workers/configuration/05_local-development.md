## Local Development

```bash
npx wrangler dev

# Test receiving
curl --request POST 'http://localhost:8787/cdn-cgi/handler/email' \
  --url-query 'from=sender@example.com' --url-query 'to=recipient@example.com' \
  --header 'Content-Type: text/plain' --data-raw 'Subject: Test\n\nHello'
```

Sent emails write to local `.eml` files.

