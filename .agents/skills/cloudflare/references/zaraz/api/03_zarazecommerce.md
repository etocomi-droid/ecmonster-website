## zaraz.ecommerce()

```javascript
zaraz.ecommerce('Product Viewed', { product_id: 'SKU123', name: 'Widget', price: 49.99 });
zaraz.ecommerce('Product Added', { product_id: 'SKU123', quantity: 2, price: 49.99 });
zaraz.ecommerce('Order Completed', {
  order_id: 'ORD-789', total: 149.98, currency: 'USD',
  products: [{ product_id: 'SKU123', quantity: 2, price: 49.99 }]
});
```

**Events:** `Product Viewed`, `Product Added`, `Product Removed`, `Cart Viewed`, `Checkout Started`, `Order Completed`

Tools auto-map to GA4, Facebook CAPI, etc.

