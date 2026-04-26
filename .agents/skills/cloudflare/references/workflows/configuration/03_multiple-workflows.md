## Multiple Workflows

```jsonc
{
  "workflows": [
    {"name": "user-onboarding", "binding": "USER_ONBOARDING", "class_name": "UserOnboarding"},
    {"name": "data-processing", "binding": "DATA_PROCESSING", "class_name": "DataProcessing"}
  ]
}
```

Each class extends `WorkflowEntrypoint` with its own `Params` type.

