## Overview

Cloudflare Workers run on V8 isolates (NOT containers/VMs):
- Extremely fast cold starts (< 1ms)
- Global deployment across 300+ locations
- Web standards compliant (fetch, URL, Headers, Request, Response)
- Support JS/TS, Python, Rust, and WebAssembly

**Key principle**: Workers use web platform APIs wherever possible for portability.

