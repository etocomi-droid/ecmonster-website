## Private Network Mode

```yaml
tunnel: <UUID>
credentials-file: /path/to/creds.json

warp-routing:
  enabled: true
```

```bash
cloudflared tunnel route ip add 10.0.0.0/8 my-tunnel
cloudflared tunnel route ip add 192.168.1.100/32 my-tunnel
```

