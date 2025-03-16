# Managing Multiple GitHub Accounts in Git

This tutorial explains how to use different GitHub accounts for different projects on Windows.

## The Problem

When you have multiple GitHub accounts (e.g., personal and work accounts), you may encounter permission issues like:

```
remote: Permission to username/repo.git denied to OtherUsername.
```

This happens because Git is using the credentials of one account when you're trying to push to a repository owned by your other account.

## Solution: Repository-Specific Configuration

### Step 1: Configure User Identity Per Repository

Git allows you to set configuration at three levels:
- System-wide (`--system`)
- Global for your user (`--global`)
- Local to a specific repository (`--local`)

To set your identity for a specific repository:

```powershell
# Navigate to your repository
cd path\to\your\repository

# Set local user name and email
git config --local user.name "YourUsername"
git config --local user.email "your-email@example.com"
```

Example:
```powershell
git config --local user.name "zagd3m"
git config --local user.email "zagd3m@gmail.com"
```

### Step 2: Configure URL-Specific Credential Storage

By default, Git stores credentials based on the domain (github.com). To store credentials based on the full repository URL:

```powershell
git config --global credential.useHttpPath true
```

This allows different credentials for different repositories, even if they're on the same domain (github.com).

### Step 3: Push to Repository

When you push to a repository for the first time after setting this up:

```powershell
git push
```

You'll be prompted for credentials. Enter the username and password (or personal access token) for the account that owns the repository.

Windows will store these credentials specifically for this repository URL, and will use them automatically for future operations.

## Checking Your Configuration

To verify which identity is being used for a repository:

```powershell
# Shows the user name configured for the current repository
git config user.name

# Shows the email configured for the current repository
git config user.email
```

## Managing Stored Credentials

Windows stores Git credentials in the Windows Credential Manager. You can view them by:

1. Open Control Panel
2. Go to User Accounts > Credential Manager
3. Look under "Windows Credentials"
4. Find entries starting with "git:" or "GitHub"

You can delete specific credentials here if you need to reset them.

## Best Practices

1. Set your most frequently used GitHub account as the global default:
   ```powershell
   git config --global user.name "DefaultUsername"
   git config --global user.email "default-email@example.com"
   ```

2. Override with local settings only in repositories where you need to use a different account.

3. Consider using SSH keys instead of HTTPS for more advanced multi-account setups.
