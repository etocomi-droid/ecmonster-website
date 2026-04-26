## Debugging Tips

1. **Log connection details:** `const info = await socket.opened; console.log(info.remoteAddress);`
2. **Test with public services first:** Use tcpbin.com:4242 echo server
3. **Verify Tunnel:** `cloudflared tunnel info <name>` and `cloudflared tunnel route ip list`

