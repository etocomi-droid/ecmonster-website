## JA3/JA4 Fingerprinting (Enterprise)

```txt
# Block specific attack fingerprint
(cf.bot_management.ja3_hash eq "8b8e3d5e3e8b3d5e")

# Allow mobile app by fingerprint
(cf.bot_management.ja4 eq "your_mobile_app_fingerprint")
```

Only available for HTTPS/TLS traffic. Missing for Worker-routed traffic or HTTP requests.

