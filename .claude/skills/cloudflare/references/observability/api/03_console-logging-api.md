### Console Logging API

**Methods**:
```typescript
// Standard methods (all appear in Workers Logs)
console.log('info message');
console.info('info message');
console.warn('warning message');
console.error('error message');
console.debug('debug message');

// Structured logging (recommended)
console.log({
  level: 'info',
  user_id: '123',
  action: 'checkout',
  amount: 99.99,
  currency: 'USD'
});
```

**Log Levels**: All console methods produce logs; use structured fields for filtering:
```typescript
console.log({ 
  level: 'error', 
  message: 'Payment failed', 
  error_code: 'CARD_DECLINED' 
});
```

