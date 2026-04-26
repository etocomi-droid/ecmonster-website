## Use Cases

**1:1:** A creates session+publishes, B creates+subscribes to A+publishes, A subscribes to B
**N:N:** All create session+publish, backend broadcasts track IDs, all subscribe to others
**1:N:** Publisher creates+publishes, viewers each create+subscribe (no fan-out limit)
**Breakout:** Same PeerConnection! Backend closes/adds tracks, no recreation

