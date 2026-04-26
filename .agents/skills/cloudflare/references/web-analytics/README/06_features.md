## Features

### Core Web Vitals Debugging
- **LCP (Largest Contentful Paint)** - Identifies slow-loading hero images/elements
- **FID (First Input Delay)** - Interaction responsiveness (legacy metric)
- **INP (Interaction to Next Paint)** - Modern interaction responsiveness metric
- **CLS (Cumulative Layout Shift)** - Visual stability issues
- **TTFB (Time to First Byte)** - Server response performance

Dashboard shows top 5 problematic elements with CSS selectors for debugging.

### Traffic Filters
- **Bot filtering** - Exclude automated traffic from metrics
- **Date ranges** - Custom time period analysis
- **Geographic** - Country-level filtering
- **Device type** - Desktop, mobile, tablet breakdown
- **Browser/OS** - User agent filtering

### Rules (Advanced - Plan-dependent)

Create custom tracking rules for advanced configurations:

**Sample Rate Rules:**
- Reduce data collection percentage for high-traffic sites
- Example: Track only 50% of visitors to reduce volume

**Path-Based Rules:**
- Different behavior per route
- Example: Exclude `/admin/*` or `/internal/*` from tracking

**Host-Based Rules:**
- Multi-domain configurations
- Example: Separate tracking for staging vs production subdomains

**Availability:** Rules feature depends on your Cloudflare plan. Check dashboard under Web Analytics → Rules to see if available. Free plans may have limited or no access.

