## Environment Isolation

Separate DO namespaces per environment (staging/production have distinct object instances):

```jsonc
{
  "durable_objects": {
    "bindings": [{ "name": "MY_DO", "class_name": "MyDO" }]
  },
  "env": {
    "production": {
      "durable_objects": {
        "bindings": [
          { "name": "MY_DO", "class_name": "MyDO", "environment": "production" }
        ]
      }
    }
  }
}
```

Deploy: `npx wrangler deploy --env production`

