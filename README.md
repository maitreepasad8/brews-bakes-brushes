# Brews, Bakes & Brushes - Static Website

A beautiful static website to host and display the "Brews, Bakes & Brushes" PDF.

## 📁 Files

- `index.html` - Main website page that displays PDF pages as images (auto-generated)
- `Brews, Bakes & Brushes (1).pdf` - The PDF document
- `convert_pdf.py` - Script to convert PDF pages to images
- `requirements.txt` - Python dependencies
- `pages/` - Directory containing converted PDF page images (created after running convert_pdf.py)

## 🚀 Quick Start

### Step 1: Convert PDF to Images

1. Install Python dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
   Or if you need a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Convert the PDF to images:
   ```bash
   python3 convert_pdf.py
   ```
   
   This will:
   - Convert each PDF page to a high-quality PNG image
   - Save images in the `pages/` directory
   - Automatically generate/update `index.html` with all pages

### Step 2: View the Website

1. Start a local server:
   ```bash
   python3 -m http.server 8000
   ```

2. Open your browser and visit:
   ```
   http://localhost:8000
   ```

### Option 2: Using Node.js (if you have it installed)

```bash
npx http-server -p 8000
```

### Option 3: Deploy to GitHub Pages

1. **Create a new GitHub repository:**
   - Go to [GitHub](https://github.com) and create a new repository
   - Name it something like `brews-bakes-brushes` (or any name you prefer)
   - Make it public (required for free GitHub Pages)
   - Don't initialize with README (we already have one)

2. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Brews, Bakes & Brushes website"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```
   Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

3. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Click on **Settings** tab
   - Scroll down to **Pages** in the left sidebar
   - Under **Source**, select **Deploy from a branch**
   - Select **main** branch and **/ (root)** folder
   - Click **Save**

4. **Your site will be live at:**
   ```
   https://YOUR_USERNAME.github.io/YOUR_REPO_NAME
   ```
   It may take a few minutes for the site to be available after enabling Pages.

## 🌐 Deployment Options

### GitHub Pages
- Free hosting
- Easy setup through repository settings
- URL format: `https://username.github.io/repo-name`

### Netlify
- Drag and drop deployment
- Free tier available
- Custom domain support

### Vercel
- Fast deployment
- Free tier available
- Great for static sites

## 📝 Notes

- The PDF pages are converted to images and displayed seamlessly as part of the website
- Each page appears as a full-width image with smooth scrolling
- The conversion script automatically generates the HTML with all pages
- Make sure the PDF file name matches exactly: `Brews, Bakes & Brushes (1).pdf`
- Image quality is set to 150 DPI by default (adjustable in `convert_pdf.py`)

## 🎨 Customization

You can customize the website by editing `index.html`:
- Change colors in the CSS
- Modify the header text
- Adjust the PDF viewer size
- Add additional content or pages

## 📄 License

© 2024 Brews, Bakes & Brushes | Created by Maitree Pasad
