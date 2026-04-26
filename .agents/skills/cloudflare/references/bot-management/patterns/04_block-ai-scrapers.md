## Block AI Scrapers

```txt
# Block training crawlers only (allow AI assistants/search)
(cf.verified_bot_category eq "AI Crawler")
Action: Block

# Block all AI-related bots (training + assistants + search)
(cf.verified_bot_category in {"AI Crawler" "AI Assistant" "AI Search"})
Action: Block

# Allow AI Search, block AI Crawler and AI Assistant
(cf.verified_bot_category in {"AI Crawler" "AI Assistant"})
Action: Block

# Or use dashboard: Security > Settings > Bot Management > Block AI Bots
```

