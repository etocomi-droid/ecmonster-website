          ...Object.fromEntries(response.headers),
          'Cache-Control': 'public, max-age=31536000, immutable'
        }
      });
    }
    return response;
  }
};
```
