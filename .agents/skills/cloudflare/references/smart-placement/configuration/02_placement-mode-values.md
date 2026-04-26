## Placement Mode Values

| Mode | Behavior |
|------|----------|
| `"smart"` | Enable Smart Placement - automatic optimization based on traffic analysis |
| `"off"` | Explicitly disable Smart Placement - always run at edge closest to user |
| Not specified | Default behavior - run at edge closest to user (same as `"off"`) |

**Note:** Smart Placement vs Explicit Placement are separate features. Smart Placement (`mode: "smart"`) uses automatic analysis. For manual placement control, see explicit placement options (`region`, `host`, `hostname` fields - not covered in this reference).

