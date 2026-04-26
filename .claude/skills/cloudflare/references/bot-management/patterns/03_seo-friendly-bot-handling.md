## SEO-Friendly Bot Handling

```txt
# Allow search engine crawlers
(cf.bot_management.score lt 30 and not cf.verified_bot_category in {"Search Engine Crawler"})
Action: Managed Challenge
```

