## Create API Token

R2 SQL requires API token with R2 permissions.

### Required Permission

**R2 Admin Read & Write** (includes R2 SQL Read permission)

### Via Dashboard

1. Navigate to **R2 Object Storage**
2. Click **Manage API tokens** (top right)
3. Click **Create API token**
4. Select **Admin Read & Write** permission
5. Click **Create API Token**
6. **Copy token value** - shown only once

### Permission Scope

| Permission | Grants Access To |
|------------|------------------|
| R2 Admin Read & Write | R2 storage operations + R2 SQL queries + Data Catalog operations |
| R2 SQL Read | SQL queries only (no storage writes) |

**Note:** R2 SQL Read permission not yet available via Dashboard - use Admin Read & Write.

