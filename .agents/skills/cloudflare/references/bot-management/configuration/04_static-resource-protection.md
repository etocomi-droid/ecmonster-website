## Static Resource Protection

**File Extensions**: ico, jpg, png, jpeg, gif, css, js, tif, tiff, bmp, pict, webp, svg, svgz, class, jar, txt, csv, doc, docx, xls, xlsx, pdf, ps, pls, ppt, pptx, ttf, otf, woff, woff2, eot, eps, ejs, swf, torrent, midi, mid, m3u8, m4a, mp3, ogg, ts  
**Plus**: `/.well-known/` path (all files)

```txt
# Exclude static resources from bot rules
(cf.bot_management.score lt 30 and not cf.bot_management.static_resource)
```

**WARNING**: May block mail clients fetching static images

