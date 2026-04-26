## Mutual TLS (mTLS)

**Setup:**
```
SSL/TLS > Client Certificates > Create Certificate
- Generate CF-managed CA (all plans)
- Upload custom CA (Enterprise, max 5)
```

**Configure mTLS rule:**
```
Security > API Shield > mTLS
- Select hostname(s)
- Choose certificate(s)
- Action: Block/Log/Challenge
```

**Test:**
```bash
openssl req -x509 -newkey rsa:4096 -keyout client-key.pem -out client-cert.pem -days 365
curl https://api.example.com/endpoint --cert client-cert.pem --key client-key.pem
```

