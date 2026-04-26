## Workers Analytics

```graphql
query WorkersOverview($accountTag: string!, $start: Time!, $end: Time!) {
  viewer {
    accounts(filter: { accountTag: $accountTag }) {
      workersInvocationsAdaptive(
        filter: { datetime_gt: $start, datetime_lt: $end }
        limit: 100
        orderBy: [sum_requests_DESC]
      ) {
        sum { requests errors subrequests wallTime }
        quantiles { cpuTimeP50 cpuTimeP99 wallTimeP50 wallTimeP99 }
        dimensions { scriptName }
      }
    }
  }
}
```

Filter by `scriptName` for a specific Worker. Add `datetimeFiveMinutes` dimension + `orderBy: [datetimeFiveMinutes_ASC]` for error rate over time.

