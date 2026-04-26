## Checking Editability Before Updates

**Critical:** Always check the `editable` field before attempting to enable/disable Argo. When `editable: false`, the zone has restrictions (billing not configured, insufficient permissions, or plan limitations).

**Pattern:**
```typescript
async function safelyEnableArgo(client: Cloudflare, zoneId: string): Promise<boolean> {
  const status = await client.argo.smartRouting.get({ zone_id: zoneId });
  
  if (!status.editable) {
    console.error('Cannot modify Argo: editable=false (check billing/permissions)');
    return false;
  }
  
  if (status.value === 'on') {
    console.log('Argo already enabled');
    return true;
  }
  
  await client.argo.smartRouting.edit({ zone_id: zoneId, value: 'on' });
  console.log('Argo enabled successfully');
  return true;
}
```

**Python Pattern:**
```python
def safely_enable_argo(client: Cloudflare, zone_id: str) -> bool:
    status = client.argo.smart_routing.get(zone_id=zone_id)
    
    if not status.editable:
        print('Cannot modify Argo: editable=false (check billing/permissions)')
        return False
    
    if status.value == 'on':
        print('Argo already enabled')
        return True
    
    client.argo.smart_routing.edit(zone_id=zone_id, value='on')
    print('Argo enabled successfully')
    return True
```

