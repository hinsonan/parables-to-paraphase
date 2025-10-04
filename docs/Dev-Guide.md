# Git Feature Branch Development Guide for College Students

## Overview
This guide explains how to develop features using Git branches, create pull requests, and collaborate effectively on our project. We use a **dev → master** workflow where all development happens through feature branches.

## Branch Structure

```
master (production-ready code)
  ↑
dev (development integration)
  ↑
feature/your-feature-name (your work)
```

### Branch Purposes
- **`master`**: Production-ready code, only updated from `dev`
- **`dev`**: Integration branch where all features merge
- **`feature/*`**: Individual feature development branches

## Step-by-Step Workflow

### 1. Start a New Feature

```bash
# Make sure you're on dev and it's up to date
git checkout dev
git pull origin dev

# Create and switch to your feature branch
git checkout -b feature/add-login-system
```

**Branch Naming Convention:**
- `feature/short-description`
- `feature/user-authentication`
- `feature/shopping-cart`
- `bugfix/fix-header-styling`

### 2. Develop Your Feature

```bash
# Make your changes and commit regularly
git add .
git commit -m "Add user login form"

git add .
git commit -m "Implement password validation"

git add .
git commit -m "Add login error handling"
```

**Good Commit Messages:**
- ✅ "Add user registration form"
- ✅ "Fix navigation menu on mobile"
- ✅ "Update database schema for users table"
- ❌ "Fixed stuff"
- ❌ "WIP"
- ❌ "asdf"

### 3. Keep Your Branch Updated

```bash
# Regularly sync with dev to avoid conflicts
git checkout dev
git pull origin dev
git checkout feature/add-login-system
git merge dev
```

### 4. Push Your Feature Branch

```bash
# Push your feature branch to GitHub
git push origin feature/add-login-system
```

### 5. Create a Pull Request

1. Go to GitHub repository
2. Click "New Pull Request"
3. Set **base branch** to `dev` (not master!)
4. Set **compare branch** to your feature branch
5. Fill out the PR template:

```markdown
## Description
Brief description of what this PR does.

## Changes Made
- Added user login form
- Implemented password validation
- Added error handling for invalid credentials

## Testing (if applicable)
- [ ] Tested login with valid credentials
- [ ] Tested login with invalid credentials
- [ ] Tested on mobile devices

## Screenshots (if applicable)
[Add screenshots of UI changes]
```

### 6. Code Review Process

1. **Request reviewers** (assign all classmates and Teacher)
2. **Address feedback** by making additional commits
3. **Never force push** after creating PR
4. **Resolve conflicts** if they arise

### 7. After PR is Merged

```bash
# Switch back to dev and pull the latest changes
git checkout dev
git pull origin dev

# Delete your local feature branch
git branch -d feature/add-login-system

# Delete remote feature branch (optional)
git push origin --delete feature/add-login-system
```

## Common Git Commands Cheat Sheet

### Basic Operations
```bash
# Check current status
git status

# See which branch you're on
git branch

# Switch branches
git checkout branch-name

# Create and switch to new branch
git checkout -b new-branch-name

# Pull latest changes
git pull origin branch-name

# Push changes
git push origin branch-name
```

### Handling Conflicts
```bash
# If you get merge conflicts:
git status                    # See which files have conflicts
# Edit the files to resolve conflicts
git add resolved-file.js      # Stage resolved files
git commit -m "Resolve merge conflicts"
```

## Best Practices

### ✅ Do This
- **Small, focused PRs** - easier to review
- **Descriptive commit messages** - explain what and why
- **Test your code** before creating PR
- **Update your branch** regularly from dev
- **Use clear branch names** that describe the feature
- **Fill out PR descriptions** completely

### ❌ Don't Do This
- **Never commit directly to `dev` or `master`**
- **Don't create massive PRs** with many unrelated changes
- **Don't force push** after creating a PR
- **Don't ignore code review feedback**

## Troubleshooting

### "I accidentally committed to dev"
```bash
# Undo the last commit (keep your changes)
git reset --soft HEAD~1

# Create a feature branch
git checkout -b feature/my-accidentally-committed-work

# Add and commit your changes
git add .
git commit -m "Properly commit my feature"
```

### "My branch is behind dev"
```bash
# Get latest dev changes
git checkout dev
git pull origin dev

# Go back to your feature branch and merge
git checkout feature/my-branch
git merge dev
```

### "I have merge conflicts"
1. Open the conflicted files in your editor
2. Look for `<<<<<<<`, `=======`, and `>>>>>>>` markers
3. Choose which version to keep or combine them
4. Remove the conflict markers
5. Save the file and commit:
```bash
git add conflicted-file.js
git commit -m "Resolve merge conflicts in user authentication"
```

## Example Workflow

Here's a complete example of adding a new feature:

```bash
# 1. Start from updated dev
git checkout dev
git pull origin dev

# 2. Create feature branch
git checkout -b feature/user-profile-page

# 3. Make changes and commit
git add src/components/Profile.js
git commit -m "Add user profile component"

git add src/styles/profile.css
git commit -m "Style user profile page"

# 4. Push and create PR
git push origin feature/user-profile-page
# Go to GitHub and create PR to dev branch

# 5. After PR is merged, clean up
git checkout dev
git pull origin dev
git branch -d feature/user-profile-page
```
