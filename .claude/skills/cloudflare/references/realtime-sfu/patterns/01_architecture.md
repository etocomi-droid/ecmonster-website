## Architecture

```
Client (WebRTC) <---> CF Edge <---> Backend (HTTP)
                           |
                    CF Backbone (310+ DCs)
                           |
                    Other Edges <---> Other Clients
```

Anycast: Last-mile <50ms (95%), no region select, NACK shield, distributed consensus

Cascading trees auto-scale to millions:
```
Publisher -> Edge A -> Edge B -> Sub1
                    \-> Edge C -> Sub2,3
```

