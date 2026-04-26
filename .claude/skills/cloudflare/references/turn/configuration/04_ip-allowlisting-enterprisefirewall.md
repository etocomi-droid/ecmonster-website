## IP Allowlisting (Enterprise/Firewall)

For strict firewalls, allowlist these IPs for `turn.cloudflare.com`:

| Type | Address | Protocol |
|------|---------|----------|
| IPv4 | 141.101.90.1/32 | All |
| IPv4 | 162.159.207.1/32 | All |
| IPv6 | 2a06:98c1:3200::1/128 | All |
| IPv6 | 2606:4700:48::1/128 | All |

**IMPORTANT**: These IPs may change with 14-day notice. Monitor DNS:

```bash
# Check A and AAAA records
dig turn.cloudflare.com A
dig turn.cloudflare.com AAAA
```

Set up automated monitoring to detect IP changes and update allowlists within 14 days.

