## Service Installation

### Linux systemd
```bash
cloudflared service install
systemctl start cloudflared && systemctl enable cloudflared
journalctl -u cloudflared -f  # Logs
```

### macOS launchd
```bash
sudo cloudflared service install
sudo launchctl start com.cloudflare.cloudflared
```
