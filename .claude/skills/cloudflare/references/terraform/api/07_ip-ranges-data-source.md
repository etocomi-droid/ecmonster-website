## IP Ranges Data Source

```hcl
# Get Cloudflare IP ranges (for firewall rules)
data "cloudflare_ip_ranges" "cloudflare" {}

output "ipv4_cidrs" {
  value = data.cloudflare_ip_ranges.cloudflare.ipv4_cidr_blocks
}

output "ipv6_cidrs" {
  value = data.cloudflare_ip_ranges.cloudflare.ipv6_cidr_blocks
}

# Use in security group rules (AWS example)
resource "aws_security_group_rule" "allow_cloudflare" {
  type = "ingress"
  from_port = 443
  to_port = 443
  protocol = "tcp"
  cidr_blocks = data.cloudflare_ip_ranges.cloudflare.ipv4_cidr_blocks
  security_group_id = aws_security_group.web.id
}
```

