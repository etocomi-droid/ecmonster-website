## API Protection

```txt
# Protect API with JS detection + score
(http.request.uri.path matches "^/api/" and (cf.bot_management.score lt 30 or not cf.bot_management.js_detection.passed) and not cf.bot_management.verified_bot)
Action: Block
```

