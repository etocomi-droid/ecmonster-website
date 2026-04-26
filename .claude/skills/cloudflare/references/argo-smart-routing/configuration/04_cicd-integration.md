## CI/CD Integration

**GitHub Actions Example:**
```yaml
# .github/workflows/deploy-argo.yml
name: Deploy Argo Configuration

on:
  push:
    branches: [main]
    paths:
      - 'terraform/argo.tf'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v2
        
      - name: Terraform Init
        run: terraform init
        working-directory: ./terraform
        
      - name: Terraform Apply
        run: terraform apply -auto-approve
        working-directory: ./terraform
        env:
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          TF_VAR_zone_id: ${{ secrets.CLOUDFLARE_ZONE_ID }}
```

