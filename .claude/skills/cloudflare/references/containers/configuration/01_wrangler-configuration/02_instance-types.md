### Instance Types

#### Predefined Types

| Type | vCPU | Memory | Disk |
|------|------|--------|------|
| lite | 1/16 | 256 MiB | 2 GB |
| basic | 1/4 | 1 GiB | 4 GB |
| standard-1 | 1/2 | 4 GiB | 8 GB |
| standard-2 | 1 | 6 GiB | 12 GB |
| standard-3 | 2 | 8 GiB | 16 GB |
| standard-4 | 4 | 12 GiB | 20 GB |

```jsonc
{
  "containers": [
    {
      "class_name": "MyContainer",
      "image": "./Dockerfile",
      "instance_type": "standard-2"  // Use predefined type
    }
  ]
}
```

#### Custom Types (Jan 2026 Feature)

```jsonc
{
  "containers": [
    {
      "class_name": "MyContainer",
      "image": "./Dockerfile",
      "instance_type_custom": {
        "vcpu": 2,              // 1-4 vCPU
        "memory_mib": 8192,     // 512-12288 MiB (up to 12 GiB)
        "disk_mib": 16384       // 2048-20480 MiB (up to 20 GB)
      }
    }
  ]
}
```

**Custom type constraints:**
- Minimum 3 GiB memory per vCPU
- Maximum 2 GB disk per 1 GiB memory
- Max 4 vCPU, 12 GiB memory, 20 GB disk per container

