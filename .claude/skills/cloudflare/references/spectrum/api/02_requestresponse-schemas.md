## Request/Response Schemas

### CreateSpectrumAppRequest

```typescript
interface CreateSpectrumAppRequest {
  protocol: string;                    // "tcp/22", "udp/53"
  dns: {
    type: "CNAME" | "ADDRESS";
    name: string;                      // "ssh.example.com"
  };
  origin_direct?: string[];            // ["tcp://192.0.2.1:22"]
  origin_dns?: { name: string };       // {"name": "origin.example.com"}
  origin_port?: number | { start: number; end: number };
  proxy_protocol?: "off" | "v1" | "v2" | "simple";
  ip_firewall?: boolean;
  tls?: "off" | "flexible" | "full" | "strict";
  edge_ips?: {
    type: "dynamic" | "static";
    connectivity: "all" | "ipv4" | "ipv6";
  };
  traffic_type?: "direct" | "http" | "https";
  argo_smart_routing?: boolean;
}
```

### SpectrumApp Response

```typescript
interface SpectrumApp {
  id: string;
  protocol: string;
  dns: { type: string; name: string };
  origin_direct?: string[];
  origin_dns?: { name: string };
  origin_port?: number | { start: number; end: number };
  proxy_protocol: string;
  ip_firewall: boolean;
  tls: string;
  edge_ips: { type: string; connectivity: string; ips?: string[] };
  argo_smart_routing: boolean;
  created_on: string;
  modified_on: string;
}
```

