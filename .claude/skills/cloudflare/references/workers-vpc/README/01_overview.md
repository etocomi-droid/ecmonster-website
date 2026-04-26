## Overview

Workers VPC connectivity enables outbound TCP connections from Workers to private resources in AWS, Azure, GCP, on-premises datacenters, or any private network. This is achieved through the **TCP Sockets API** (`cloudflare:sockets`), which provides low-level network access for custom protocols and services.

**Key capabilities:**
- Direct TCP connections to private IPs and hostnames
- TLS/StartTLS support for encrypted connections
- Integration with Cloudflare Tunnel for secure private network access
- Full control over wire protocols (database protocols, SSH, MQTT, custom TCP)

**Note:** This reference documents the TCP Sockets API. For the newer Workers VPC Services product (HTTP-only service bindings with built-in SSRF protection), refer to separate documentation when available. VPC Services is currently in beta (2025+).

