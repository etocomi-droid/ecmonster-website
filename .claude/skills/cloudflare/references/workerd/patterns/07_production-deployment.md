## Production Deployment

### Compiled Binary (Recommended)
```bash
workerd compile config.capnp myConfig -o production-server
./production-server
```

### Docker
```dockerfile
FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y ca-certificates
COPY workerd /usr/local/bin/
COPY config.capnp /etc/workerd/
COPY src/ /etc/workerd/src/
EXPOSE 8080
CMD ["workerd", "serve", "/etc/workerd/config.capnp"]
```

### Systemd
```ini
# /etc/systemd/system/workerd.service
[Service]
ExecStart=/usr/bin/workerd serve /etc/workerd/config.capnp --socket-fd http=3
Restart=always
User=nobody
```

See systemd socket activation docs for complete setup.

