## Point-in-Time Recovery

```typescript
await this.ctx.storage.getCurrentBookmark();
await this.ctx.storage.getBookmarkForTime(Date.now() - 2 * 24 * 60 * 60 * 1000);
await this.ctx.storage.onNextSessionRestoreBookmark(bookmark);
this.ctx.abort(); // Restart to apply; bookmarks lexically comparable (earlier < later)
```

