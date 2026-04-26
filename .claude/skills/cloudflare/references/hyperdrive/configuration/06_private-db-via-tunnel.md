## Private DB via Tunnel

```
Worker → Hyperdrive → Access → Tunnel → Private Network → DB
```

**Setup:**
```bash
# 1. Create tunnel
cloudflared tunnel create my-db-tunnel

# 2. Configure hostname in Zero Trust dashboard
#    Domain: db-tunnel.example.com
#    Service: TCP -> localhost:5432

# 3. Create service token (Zero Trust > Service Auth)
#    Save Client ID/Secret

# 4. Create Access app (db-tunnel.example.com)
#    Policy: Service Auth token from step 3

# 5. Create Hyperdrive
npx wrangler hyperdrive create my-private-db \
  --host=db-tunnel.example.com \
  --user=dbuser --password=dbpass --database=prod \
  --access-client-id=<ID> --access-client-secret=<SECRET>
```

**⚠️ Don't specify `--port` with Tunnel** - port configured in tunnel service settings.

