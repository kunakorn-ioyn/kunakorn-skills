---
name: aapanel-git-autodeploy
description: Automate, configure, and troubleshoot CI/CD auto-deployment from GitHub to aaPanel web servers via aaPanel WebHook. Use when setting up git push auto-deployment on aaPanel, connecting GitHub repos to aaPanel websites, or resolving aaPanel WebHook errors like '$HOME not set', 'dubious ownership', 'Permission denied', or 'No such remote origin'.
---

# aaPanel Git Auto-Deploy Workflow

This skill provides a bulletproof, battle-tested standard for setting up real-time Continuous Deployment (CI/CD) from **GitHub** to **aaPanel** web servers using the **aaPanel WebHook** plugin and GitHub Webhooks.

---

## 🎯 Architecture & Workflow

```
[Local PC] --- git push ---> [GitHub Repo] --- Webhook POST ---> [aaPanel WebHook] ---> [Auto git pull on Server]
```

Every time you run `git push origin main` on your local computer, GitHub instantly fires an HTTP POST request to aaPanel's WebHook service. aaPanel then executes a root-level shell script that safely pulls the latest code and applies proper file permissions.

---

## 🚀 Step-by-Step Setup Guide

### Step 1: Generate GitHub Personal Access Token (PAT)
*(Recommended over SSH keys because aaPanel WebHook runs in an isolated root shell without default user SSH keys)*

1. Open GitHub Token settings: [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token** $\rightarrow$ **Generate new token (classic)**
3. **Note:** `aapanel-deploy`
4. **Expiration:** `No expiration` (or desired timeframe)
5. **Scopes:** Check **`repo`** (Full control of private repositories)
6. Click **Generate token** and copy the resulting `ghp_...` token.

---

### Step 2: Install aaPanel WebHook App

1. Log in to your **aaPanel Web Dashboard**.
2. Go to **App Store** $\rightarrow$ Search for **`WebHook`** $\rightarrow$ Click **Install**.
3. Open the **WebHook** app from the Installed tab $\rightarrow$ Click **Add WebHook**.

---

### Step 3: Insert the Bulletproof Deploy Script

Paste this script into the WebHook task editor:

```bash
#!/bin/bash
# ==========================================
# aaPanel Git Auto-Deploy Script
# ==========================================

# 1. Fix Linux environment variables (Prevents '$HOME not set' error)
export HOME=/root
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 2. Project & Repository Configuration
GITHUB_TOKEN="YOUR_GITHUB_TOKEN_HERE"  # e.g., ghp_xxxxxxxxxxxxxxxxxxxx
GITHUB_OWNER="YOUR_GITHUB_USERNAME"     # e.g., ioynnightwalkerfly
GITHUB_REPO="YOUR_REPO_NAME"           # e.g., vumedlearnplan
BRANCH_NAME="main"                     # e.g., main or master
TARGET_DIR="/www/wwwroot/your-domain.com/path" # Web folder path on aaPanel

REPO_URL="https://${GITHUB_TOKEN}@github.com/${GITHUB_OWNER}/${GITHUB_REPO}.git"

echo "=== Start Auto Setup & Deploy ==="

# 3. Unlock safe.directory for Git
git config --global --add safe.directory "*"

# 4. Navigate to website directory
mkdir -p $TARGET_DIR
cd $TARGET_DIR

# 5. Initialize or reset Git remote origin
if [ ! -d ".git" ]; then
    echo "Initializing Git Repository..."
    git init
fi

git remote remove origin 2>/dev/null || true
git remote add origin $REPO_URL

# 6. Fetch & Hard-Reset to Latest Commit
echo "Fetching from GitHub..."
git fetch origin $BRANCH_NAME
git reset --hard origin/$BRANCH_NAME
git branch -M $BRANCH_NAME 2>/dev/null || true
git branch --set-upstream-to=origin/$BRANCH_NAME $BRANCH_NAME 2>/dev/null || true
git pull origin $BRANCH_NAME

# 7. Set Web Server Permissions (Nginx / Apache)
chown -R www:www $TARGET_DIR
chmod -R 755 $TARGET_DIR

echo "=== Deploy Completed Successfully ==="
```

Click **Submit / Save**.

---

### Step 4: Construct the Payload URL & Test

aaPanel provides a WebHook trigger URL in the format:
```text
http://YOUR_SERVER_IP_OR_DOMAIN:AAPANEL_PORT/hook?access_key=YOUR_ACCESS_KEY
```

1. **Test in Browser**: Paste this URL in your browser. It should return:
   `{"code": 1}`
2. **Verify Logs in aaPanel**: Open aaPanel WebHook $\rightarrow$ Click **Log** to verify `=== Deploy Completed Successfully ===`.

---

### Step 5: Configure GitHub Webhook

1. Go to your **GitHub Repository** $\rightarrow$ **Settings** $\rightarrow$ **Webhooks** $\rightarrow$ **Add webhook**.
2. **Payload URL:** Paste your aaPanel WebHook URL.
3. **Content type:** Select `application/json`.
4. **Which events would you like to trigger this webhook?:** Select `Just the push event.`
5. **Active:** Checked.
6. Click **Add webhook**.

---

## 🔒 Security Best Practices (Sensitive Configuration Isolation)

Never commit sensitive environment files (`config.env.php`, `.env`, database passwords) to GitHub.

1. Keep them in `.gitignore`:
   ```gitignore
   config.env.php
   .env
   *.log
   ```
2. Create the production `config.env.php` or `.env` manually once on the server in `$TARGET_DIR`.
3. Because the deploy script uses `git reset --hard origin/main`, untracked gitignored files like `config.env.php` will be **preserved safely without deletion**.

---

## 🛠️ Troubleshooting Guide

| Error in aaPanel WebHook Log | Root Cause | Solution |
| :--- | :--- | :--- |
| `fatal: $HOME not set` | aaPanel runs scripts in an isolated shell without standard environment variables | Add `export HOME=/root` and standard `export PATH=...` at the top of the script |
| `fatal: detected dubious ownership` | Git security restriction when running as a different Linux user | Run `git config --global --add safe.directory "*"` before executing git commands |
| `Permission denied (publickey)` | SSH key mismatch between `sysadmin` and `root` | Switch to GitHub Personal Access Token (HTTPS URL: `https://TOKEN@github.com/...`) |
| `error: No such remote 'origin'` | `.git` was initialized without a remote or with a broken remote | Run `git remote remove origin 2>/dev/null \|\| true` then `git remote add origin $REPO_URL` |
| `ambiguous argument 'origin/main'` | Local branch does not know about remote branches yet | Run `git fetch origin main` followed by `git reset --hard origin/main` |
