## Metadata Versioning

```typescript
interface VersionedData {
  version: number;
  data: any;
}

async function migrateIfNeeded(env: Env, key: string) {
  const result = await env.DATA.getWithMetadata(key, "json");
  
  if (!result.value) return null;
  
  const currentVersion = result.metadata?.version || 1;
  const targetVersion = 2;
  
  if (currentVersion < targetVersion) {
    // Migrate data format
    const migrated = migrate(result.value, currentVersion, targetVersion);
    
    // Store with new version
    await env.DATA.put(key, JSON.stringify(migrated), {
      metadata: { version: targetVersion, migratedAt: Date.now() }
    });
    
    return migrated;
  }
  
  return result.value;
}

function migrate(data: any, from: number, to: number): any {
  if (from === 1 && to === 2) {
    // V1 → V2: Rename field
    return { ...data, userName: data.name };
  }
  return data;
}
```

