# GitHub Repository Setup Instructions

Your local repository is ready! Follow these steps to push it to GitHub:

## Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Enter a repository name (e.g., "Class" or "python-class")
3. Choose Public or Private
4. **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

## Step 2: Connect and Push

After creating the repository, GitHub will show you commands. Use these commands (replace YOUR_USERNAME and REPO_NAME with your actual values):

```bash
cd "C:\Users\Manav\Desktop\Class"
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

## Alternative: If you prefer SSH

If you have SSH keys set up with GitHub:

```bash
git remote add origin git@github.com:YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

## Quick Setup Script

After creating the repo on GitHub, you can also tell me the repository URL and I can help you push it!
