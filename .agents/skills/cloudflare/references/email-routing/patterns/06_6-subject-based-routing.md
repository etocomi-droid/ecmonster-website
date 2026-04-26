## 6. Subject-Based Routing

```typescript
export default {
  async email(message, env, ctx) {
    const subject = message.headers.get("subject")?.toLowerCase() || "";
    
    if (subject.includes("[urgent]")) {
      await message.forward("oncall@corp.com");
    } else if (subject.includes("[billing]")) {
      await message.forward("billing@corp.com");
    } else if (subject.includes("[support]")) {
      await message.forward("support@corp.com");
    } else {
      await message.forward("general@corp.com");
    }
  }
} satisfies ExportedHandler;
```

