## WAF Fields Reference

```txt
# Score fields
cf.bot_management.score                    # 0-99 (0 = not computed)
cf.bot_management.verified_bot             # boolean
cf.bot_management.static_resource          # boolean
cf.bot_management.ja3_hash                 # string (Enterprise)
cf.bot_management.ja4                      # string (Enterprise)
cf.bot_management.detection_ids            # array
cf.bot_management.js_detection.passed      # boolean
cf.bot_management.corporate_proxy          # boolean (Enterprise)
cf.verified_bot_category                   # string

# Workers equivalent
request.cf.botManagement.score
request.cf.botManagement.verifiedBot
request.cf.botManagement.ja3Hash
request.cf.botManagement.ja4
request.cf.botManagement.jsDetection.passed
request.cf.verifiedBotCategory
```

