## Cost Optimization

### Cost Calculator

```typescript
interface CacheReserveEstimate {
  avgAssetSizeGB: number;
  uniqueAssets: number;
  monthlyReads: number;
  monthlyWrites: number;
  originEgressCostPerGB: number; // e.g., AWS: $0.09/GB
}

function estimateMonthlyCost(input: CacheReserveEstimate) {
  // Cache Reserve pricing
  const storageCostPerGBMonth = 0.015;
  const classAPerMillion = 4.50; // writes
  const classBPerMillion = 0.36; // reads
  
  // Calculate Cache Reserve costs
  const totalStorageGB = input.avgAssetSizeGB * input.uniqueAssets;
  const storageCost = totalStorageGB * storageCostPerGBMonth;
  const writeCost = (input.monthlyWrites / 1_000_000) * classAPerMillion;
  const readCost = (input.monthlyReads / 1_000_000) * classBPerMillion;
  
  const cacheReserveCost = storageCost + writeCost + readCost;
  
  // Calculate origin egress cost (what you'd pay without Cache Reserve)
  const totalTrafficGB = (input.monthlyReads * input.avgAssetSizeGB);
  const originEgressCost = totalTrafficGB * input.originEgressCostPerGB;
  
  // Savings calculation
  const savings = originEgressCost - cacheReserveCost;
  const savingsPercent = ((savings / originEgressCost) * 100).toFixed(1);
  
  return {
    cacheReserveCost: `$${cacheReserveCost.toFixed(2)}`,
    originEgressCost: `$${originEgressCost.toFixed(2)}`,
    monthlySavings: `$${savings.toFixed(2)}`,
    savingsPercent: `${savingsPercent}%`,
    breakdown: {
      storage: `$${storageCost.toFixed(2)}`,
      writes: `$${writeCost.toFixed(2)}`,
      reads: `$${readCost.toFixed(2)}`,
    }
  };
}

// Example: Media library
const mediaLibrary = estimateMonthlyCost({
  avgAssetSizeGB: 0.005, // 5MB images
  uniqueAssets: 10_000,
  monthlyReads: 5_000_000,
  monthlyWrites: 50_000,
  originEgressCostPerGB: 0.09, // AWS S3
});

console.log(mediaLibrary);
// {
//   cacheReserveCost: "$9.98",
//   originEgressCost: "$25.00",
//   monthlySavings: "$15.02",
//   savingsPercent: "60.1%",
//   breakdown: { storage: "$0.75", writes: "$0.23", reads: "$9.00" }
// }
```

### Optimization Guidelines

- **Set appropriate TTLs**: 10hr minimum, 24hr+ optimal for stable content, 30d max cautiously
- **Cache high-value stable assets**: Images, media, fonts, archives, documentation
- **Exclude frequently changing**: APIs, user-specific content, real-time data
- **Compression note**: Cache Reserve fetches uncompressed from origin, serves compressed to visitors - factor in origin egress costs

