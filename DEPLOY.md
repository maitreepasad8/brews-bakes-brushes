# Deploy to GitHub Pages

Your repository is ready to be pushed to GitHub! Follow these steps:

## Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **+** icon in the top right and select **New repository**
3. Name your repository (e.g., `brews-bakes-brushes`)
4. Make it **Public** (required for free GitHub Pages)
5. **Don't** initialize with README, .gitignore, or license (we already have these)
6. Click **Create repository**

## Step 2: Push Your Code

Run these commands (replace `YOUR_USERNAME` and `YOUR_REPO_NAME`):

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

For example, if your username is `maitree` and repo is `brews-bakes-brushes`:
```bash
git remote add origin https://github.com/maitree/brews-bakes-brushes.git
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** (top menu)
3. Scroll down and click **Pages** in the left sidebar
4. Under **Source**, select:
   - **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
5. Click **Save**

## Step 4: Access Your Website

Your site will be live at:
```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME
```

**Note:** It may take 1-2 minutes for the site to be available after enabling Pages. You'll see a green checkmark when it's ready.

## Updating Your Site

After making changes:
```bash
git add .
git commit -m "Update website"
git push
```

Changes will be live within a few minutes!
