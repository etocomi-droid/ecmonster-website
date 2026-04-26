## Go SDK

```go
import "github.com/cloudflare/cloudflare-go"

api, _ := cloudflare.NewWithAPIToken("your-api-token")

// Create
app, _ := api.CreateSpectrumApplication(ctx, "zone-id", cloudflare.SpectrumApplication{
    Protocol:         "tcp/22",
    DNS:              cloudflare.SpectrumApplicationDNS{Type: "CNAME", Name: "ssh.example.com"},
    OriginDirect:     []string{"tcp://192.0.2.1:22"},
    IPFirewall:       true,
    ArgoSmartRouting: true,
})

// List
apps, _ := api.SpectrumApplications(ctx, "zone-id")

// Delete
_ = api.DeleteSpectrumApplication(ctx, "zone-id", app.ID)
```

