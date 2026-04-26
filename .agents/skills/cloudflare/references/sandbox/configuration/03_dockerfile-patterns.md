## Dockerfile Patterns

**Basic**:
```dockerfile
FROM docker.io/cloudflare/sandbox:latest
RUN pip3 install --no-cache-dir pandas numpy
EXPOSE 8080  # Required for wrangler dev
```

**Scientific**:
```dockerfile
FROM docker.io/cloudflare/sandbox:latest
RUN pip3 install --no-cache-dir \
    jupyter-server ipykernel matplotlib \
    pandas seaborn plotly scipy scikit-learn
```

**Node.js**:
```dockerfile
FROM docker.io/cloudflare/sandbox:latest
RUN npm install -g typescript ts-node
```

**CRITICAL**: `EXPOSE` required for `wrangler dev` port access. Production auto-exposes all ports.

