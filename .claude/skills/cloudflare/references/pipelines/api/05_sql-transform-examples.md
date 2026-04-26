## SQL Transform Examples

### Filter Events

```sql
INSERT INTO my_sink
SELECT * FROM my_stream
WHERE event_type = 'purchase' AND amount > 100
```

### Select Specific Fields

```sql
INSERT INTO my_sink
SELECT user_id, event_type, timestamp, amount
FROM my_stream
```

### Transform and Enrich

```sql
INSERT INTO my_sink
SELECT
  user_id,
  UPPER(event_type) as event_type,
  timestamp,
  amount * 1.1 as amount_with_tax,
  CONCAT(user_id, '_', product_id) as unique_key,
  CASE
    WHEN amount > 1000 THEN 'high_value'
    WHEN amount > 100 THEN 'medium_value'
    ELSE 'low_value'
  END as customer_tier
FROM my_stream
WHERE event_type IN ('purchase', 'refund')
```

