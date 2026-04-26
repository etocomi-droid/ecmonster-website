## Report Generation

```typescript
export default {
  async scheduled(controller, env, ctx) {
    const startOfWeek = new Date(); startOfWeek.setDate(startOfWeek.getDate() - 7);
    const { results } = await env.DB.prepare(`SELECT date, revenue, orders FROM daily_stats WHERE date >= ? ORDER BY date`).bind(startOfWeek.toISOString()).all();
    const report = {period: "weekly", totalRevenue: results.reduce((sum, d) => sum + d.revenue, 0), totalOrders: results.reduce((sum, d) => sum + d.orders, 0), dailyBreakdown: results};
    const reportKey = `reports/weekly-${Date.now()}.json`;
    await env.REPORTS_BUCKET.put(reportKey, JSON.stringify(report));
    ctx.waitUntil(env.SEND_EMAIL.fetch("https://example.com/send", {method: "POST", body: JSON.stringify({to: "team@example.com", subject: "Weekly Report", reportUrl: `https://reports.example.com/${reportKey}`})}));
  },
};
```

