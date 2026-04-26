## Verified Bot Categories

```txt
# Allow search engines only
(cf.verified_bot_category eq "Search Engine Crawler")

# Block AI crawlers
(cf.verified_bot_category eq "AI Crawler")
Action: Block

# Or use dashboard: Security > Settings > Bot Management > Block AI Bots
```

| Category | String Value | Example |
|----------|--------------|---------|
| AI Crawler | `AI Crawler` | GPTBot, Claude-Web |
| AI Assistant | `AI Assistant` | Perplexity-User, DuckAssistBot |
| AI Search | `AI Search` | OAI-SearchBot |
| Accessibility | `Accessibility` | Accessible Web Bot |
| Academic Research | `Academic Research` | Library of Congress |
| Advertising & Marketing | `Advertising & Marketing` | Google Adsbot |
| Aggregator | `Aggregator` | Pinterest, Indeed |
| Archiver | `Archiver` | Internet Archive, CommonCrawl |
| Feed Fetcher | `Feed Fetcher` | RSS/Podcast updaters |
| Monitoring & Analytics | `Monitoring & Analytics` | Uptime monitors |
| Page Preview | `Page Preview` | Facebook/Slack link preview |
| SEO | `Search Engine Optimization` | Google Lighthouse |
| Security | `Security` | Vulnerability scanners |
| Social Media Marketing | `Social Media Marketing` | Brandwatch |
| Webhooks | `Webhooks` | Payment processors |
| Other | `Other` | Uncategorized bots |

