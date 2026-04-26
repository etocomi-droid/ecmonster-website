### 3. MQTT Broker

IoT device communication.

**TypeScript:**
```typescript
const mqttApp = await client.spectrum.apps.create({
  zone_id: 'your-zone-id',
  protocol: 'tcp/8883',  // Use 1883 for plain MQTT
  dns: { type: 'CNAME', name: 'mqtt.example.com' },
  origin_direct: ['tcp://mqtt-broker.internal:8883'],
  tls: 'full',  // Use 'off' for plain MQTT
});
```

**Benefits:** DDoS protection, hide broker IP, TLS termination at edge

