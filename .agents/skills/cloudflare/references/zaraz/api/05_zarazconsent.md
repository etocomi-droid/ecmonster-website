## zaraz.consent

```javascript
// Check
const purposes = zaraz.consent.getAll(); // { analytics: true, marketing: false }

// Set
zaraz.consent.modal = true; // Show modal
zaraz.consent.setAll({ analytics: true, marketing: false });
zaraz.consent.set('marketing', true);

// Listen
zaraz.consent.addEventListener('consentChanged', () => {
  if (zaraz.consent.getAll().marketing) zaraz.track('marketing_consent_granted');
});
```

**Flow:** Configure purposes in dashboard → Map tools to purposes → Show modal/set programmatically → Tools fire when allowed

