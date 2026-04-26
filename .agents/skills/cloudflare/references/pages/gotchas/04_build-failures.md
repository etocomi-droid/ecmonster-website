## Build Failures

**Problem**: Deployment fails during build  
**Causes**: Wrong build command/output dir; Node version incompatibility; missing env vars; 20min timeout; OOM  
**Solution**: Check Dashboard → Deployments → Build log; verify settings; add `.nvmrc`; optimize build

