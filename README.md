# Brews, Bakes & Brushes - Static Website

A simple static website to display images in a vertical scrolling layout.

## 📁 Files

- `index.html` - Main website page that displays images
- `pages/` - Directory containing the image files

## 🚀 Quick Start

### View Locally

1. Start a local server:
   ```bash
   python3 -m http.server 8000
   ```

2. Open your browser and visit:
   ```
   http://localhost:8000
   ```

### Using Node.js (if you have it installed)

```bash
npx http-server -p 8000
```

## 🌐 Deploy to GitHub Pages

See `DEPLOY.md` for detailed instructions on deploying to GitHub Pages.

## 📝 Adding More Images

To add more images:
1. Add your image files to the `pages/` directory
2. Edit `index.html` and add a new `<div class="page">` section for each image:
   ```html
   <div class="page">
       <img src="pages/your-image.png" alt="Page X" loading="lazy">
   </div>
   ```

## 📄 License

© 2024 Brews, Bakes & Brushes | Created by Maitree Pasad