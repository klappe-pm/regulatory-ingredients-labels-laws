# Keychain-Based Environment Variable Setup

Complete documentation for secure API key management using macOS Keychain.

## Table of Contents
1. [Overview](#overview)
2. [What Was Set Up](#what-was-set-up)
3. [How It Works](#how-it-works)
4. [Testing Your Setup](#testing-your-setup)
5. [Troubleshooting](#troubleshooting)
6. [Adding New API Keys](#adding-new-api-keys)
7. [Security Best Practices](#security-best-practices)
8. [Production Deployment](#production-deployment)

---

## Overview

Your API keys are now securely stored in macOS Keychain and automatically loaded as environment variables for:
- **Terminal sessions** (bash/zsh)
- **Claude Desktop** (GUI application)
- **Claude Code CLI** (terminal command)
- **All development projects**

### API Keys Managed
- `ANTHROPIC_API_KEY` - Claude AI models
- `OPENROUTER_API_KEY` - Multi-model API access
- `GOOGLE_API_KEY` - Google Gemini/AI services
- `XAI_API_KEY` - X.AI Grok models
- `OPENAI_API_KEY` - OpenAI GPT models
- `CLAUDE_API_KEY` - Claude Code MCP server
- `PORT` - MCP server port (27126)
- `AWS_REGION` - AWS default region (us-east-1)

### AWS Credentials
AWS credentials are managed separately via `~/.aws/credentials` (standard AWS approach).

---

## What Was Set Up

### 1. **Keychain Loader Script**
**Location:** `~/bin/load-keychain-env.sh`

Retrieves API keys from keychain and exports them as environment variables.

### 2. **LaunchAgent**
**Location:** `~/Library/LaunchAgents/com.user.keychain-env.plist`

Runs at login to make API keys available to GUI applications like Claude Desktop.

### 3. **Shell Profiles Updated**
- `~/.bash_profile` - Bash shell configuration
- `~/.zshrc` - Zsh shell configuration

Both now source the keychain loader script automatically.

### 4. **Claude Desktop Configuration**
**Location:** `~/Library/Application Support/Claude/claude_desktop_config.json`

Updated to use environment variables instead of hardcoded API keys.

### 5. **Production Template**
**Location:** `~/.env.example`

Template for project-specific environment configuration.

---

## How It Works

### For Terminal Sessions (bash/zsh)
1. You open a new terminal
2. Shell profile (`.bash_profile` or `.zshrc`) runs automatically
3. `~/bin/load-keychain-env.sh` is sourced
4. Script retrieves keys from keychain
5. Keys are exported as environment variables
6. All terminal commands now have access to API keys

### For GUI Applications (Claude Desktop)
1. You log in to macOS
2. LaunchAgent (`com.user.keychain-env.plist`) runs automatically
3. Script retrieves keys from keychain
4. Keys are set system-wide via `launchctl setenv`
5. Claude Desktop and other apps can access the keys

### For AWS
AWS credentials are read from `~/.aws/credentials` by AWS CLI and all AWS MCP servers.

---

## Testing Your Setup

### Test 1: Terminal Access

Open a **new terminal** and run:

```bash
# Source the environment loader (should happen automatically)
source ~/bin/load-keychain-env.sh

# Test with debug mode
KEYCHAIN_ENV_DEBUG=true source ~/bin/load-keychain-env.sh
```

You should see output like:
```
✓ Loaded API keys from keychain:
  - ANTHROPIC_API_KEY: sk-ant-api03-544c3c-...
  - OPENROUTER_API_KEY: sk-or-v1-22735aa8129...
  - GOOGLE_API_KEY: AIzaSyANmppyWVFvVzwA...
  - XAI_API_KEY: xai-iexAXXLqEyMBlyQV...
  - OPENAI_API_KEY: sk-proj-Lp03BgFA81Ap...
  - CLAUDE_API_KEY: sk-ant-api03-544c3c-...
  - PORT: 27126
  - AWS_REGION: us-east-1
```

### Test 2: Verify Individual Keys

```bash
# Check each key is set (without revealing the full value)
echo "ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:0:20}..."
echo "OPENROUTER_API_KEY: ${OPENROUTER_API_KEY:0:20}..."
echo "GOOGLE_API_KEY: ${GOOGLE_API_KEY:0:20}..."
echo "XAI_API_KEY: ${XAI_API_KEY:0:20}..."
echo "OPENAI_API_KEY: ${OPENAI_API_KEY:0:20}..."
echo "CLAUDE_API_KEY: ${CLAUDE_API_KEY:0:20}..."
echo "PORT: ${PORT}"
echo "AWS_REGION: ${AWS_REGION}"
```

### Test 3: AWS Credentials

```bash
aws sts get-caller-identity
```

Should output your AWS account information.

### Test 4: LaunchAgent Status

```bash
# Check if LaunchAgent is loaded
launchctl list | grep com.user.keychain-env

# Check LaunchAgent logs
cat /tmp/keychain-env.log
cat /tmp/keychain-env.error.log
```

### Test 5: Claude Desktop

1. **Quit Claude Desktop completely** (Cmd+Q)
2. **Reopen Claude Desktop**
3. Try using a feature that requires API keys (e.g., zen MCP server)

---

## Troubleshooting

### Problem: Keys not available in new terminal

**Solution:**
```bash
# Manually source the loader script
source ~/bin/load-keychain-env.sh

# Check if script exists and is executable
ls -la ~/bin/load-keychain-env.sh
```

### Problem: Claude Desktop can't access keys

**Solutions:**

1. **Reload the LaunchAgent:**
```bash
launchctl unload ~/Library/LaunchAgents/com.user.keychain-env.plist
launchctl load ~/Library/LaunchAgents/com.user.keychain-env.plist
```

2. **Check LaunchAgent logs:**
```bash
cat /tmp/keychain-env.log
cat /tmp/keychain-env.error.log
```

3. **Restart Claude Desktop:**
- Quit Claude Desktop completely (Cmd+Q)
- Reopen it

4. **Restart your Mac** (last resort - ensures LaunchAgent runs cleanly)

### Problem: AWS commands not working

**Solution:**
```bash
# Verify AWS credentials file exists
cat ~/.aws/credentials

# Test AWS configuration
aws configure list

# Test AWS authentication
aws sts get-caller-identity
```

### Problem: Keys are empty or not found

**Solution:**
```bash
# Verify keys exist in keychain
security find-generic-password -a "${USER}" -s "ANTHROPIC_API_KEY"

# Retrieve a key manually to test
security find-generic-password -a "${USER}" -s "ANTHROPIC_API_KEY" -w
```

### Problem: Permission denied accessing keychain

**Solution:**
- Open **Keychain Access** app
- Click on **login** keychain
- Find the API key entries
- Right-click → **Get Info**
- Go to **Access Control** tab
- Add `/bin/bash` and `/bin/zsh` to allowed applications

---

## Adding New API Keys

### Step 1: Add to Keychain

```bash
# Add the new key
security add-generic-password -a "${USER}" -s "NEW_API_KEY_NAME" -w
# You'll be prompted to paste the key value (input hidden)
```

### Step 2: Update Loader Script

Edit `~/bin/load-keychain-env.sh` and add:

```bash
export NEW_API_KEY_NAME=$(get_keychain_value "NEW_API_KEY_NAME")
```

### Step 3: Update LaunchAgent

Edit `~/Library/LaunchAgents/com.user.keychain-env.plist` and add:

```xml
export NEW_API_KEY_NAME=$(security find-generic-password -a "$USER" -s "NEW_API_KEY_NAME" -w 2>/dev/null)

launchctl setenv NEW_API_KEY_NAME "$NEW_API_KEY_NAME"
```

### Step 4: Reload Configuration

```bash
# Reload LaunchAgent
launchctl unload ~/Library/LaunchAgents/com.user.keychain-env.plist
launchctl load ~/Library/LaunchAgents/com.user.keychain-env.plist

# Reload terminal
source ~/bin/load-keychain-env.sh
```

---

## Security Best Practices

### ✅ DO:
- ✅ Rotate API keys every 90 days
- ✅ Use different keys for development and production
- ✅ Limit key permissions to minimum required scope
- ✅ Monitor key usage for suspicious activity
- ✅ Backup your keychain (it's encrypted)
- ✅ Use MFA on API provider accounts
- ✅ Keep macOS and Keychain Access updated

### ❌ DON'T:
- ❌ Share API keys via email, Slack, or other messaging
- ❌ Commit API keys to version control (Git)
- ❌ Store keys in plain text files
- ❌ Use production keys in development
- ❌ Give keys broader permissions than needed
- ❌ Reuse the same key across multiple services

### Key Rotation Process

1. **Generate new key** from API provider
2. **Add to keychain** using same key name (overwrites old value)
3. **Test** that new key works
4. **Revoke old key** from API provider dashboard
5. **Update** any external documentation

```bash
# To update a key in keychain (will prompt for new value)
security add-generic-password -a "${USER}" -s "ANTHROPIC_API_KEY" -w -U
```

### Backup Your Keychain

```bash
# Export keychain (creates encrypted backup)
# Store this file securely (e.g., password manager, encrypted drive)
cp ~/Library/Keychains/login.keychain-db ~/Backups/keychain-backup-$(date +%Y%m%d).keychain-db
```

---

## Production Deployment

For production environments, **DO NOT** use macOS Keychain. Instead, use:

### Option 1: AWS Secrets Manager

```bash
# Store secrets
aws secretsmanager create-secret \
  --name prod/api-keys \
  --description "Production API keys" \
  --secret-string file://.env

# Retrieve in application
aws secretsmanager get-secret-value \
  --secret-id prod/api-keys \
  --query SecretString \
  --output text
```

### Option 2: Google Cloud Secret Manager

```bash
# Store secrets
gcloud secrets create api-keys --data-file=.env

# Retrieve in application
gcloud secrets versions access latest --secret="api-keys"
```

### Option 3: HashiCorp Vault

```bash
# Store secrets
vault kv put secret/prod/api-keys @.env

# Retrieve in application
vault kv get -field=ANTHROPIC_API_KEY secret/prod/api-keys
```

### Option 4: Environment Variables (Kubernetes, Docker)

```yaml
# Kubernetes Secret
apiVersion: v1
kind: Secret
metadata:
  name: api-keys
type: Opaque
stringData:
  ANTHROPIC_API_KEY: sk-ant-api03-xxxxx
  OPENAI_API_KEY: sk-proj-xxxxx
```

```bash
# Docker
docker run --env-file .env myapp

# Docker Compose
services:
  myapp:
    env_file:
      - .env
```

### Project-Specific .env File

1. **Copy template** to your project:
```bash
cp ~/.env.example /path/to/your/project/.env
```

2. **Edit** `.env` and fill in actual values

3. **Add to `.gitignore`**:
```bash
echo ".env" >> /path/to/your/project/.gitignore
```

4. **Load in your application:**

Python:
```python
from dotenv import load_dotenv
load_dotenv()

import os
api_key = os.getenv('ANTHROPIC_API_KEY')
```

Node.js:
```javascript
require('dotenv').config();

const apiKey = process.env.ANTHROPIC_API_KEY;
```

---

## Quick Reference

### Useful Commands

```bash
# Reload terminal environment
source ~/.bash_profile  # or ~/.zshrc

# Reload LaunchAgent
launchctl unload ~/Library/LaunchAgents/com.user.keychain-env.plist
launchctl load ~/Library/LaunchAgents/com.user.keychain-env.plist

# Test keychain loader with debug output
KEYCHAIN_ENV_DEBUG=true source ~/bin/load-keychain-env.sh

# List all keys in keychain
security find-generic-password -a "${USER}" -s "ANTHROPIC_API_KEY"
security find-generic-password -a "${USER}" -s "OPENROUTER_API_KEY"
security find-generic-password -a "${USER}" -s "GOOGLE_API_KEY"
security find-generic-password -a "${USER}" -s "XAI_API_KEY"
security find-generic-password -a "${USER}" -s "OPENAI_API_KEY"
security find-generic-password -a "${USER}" -s "CLAUDE_API_KEY"

# Test AWS
aws sts get-caller-identity
aws configure list

# Check environment variables
env | grep -E "ANTHROPIC|OPENAI|GOOGLE|XAI|OPENROUTER|CLAUDE|AWS"
```

### File Locations

| Component | Location |
|-----------|----------|
| Keychain Loader Script | `~/bin/load-keychain-env.sh` |
| LaunchAgent | `~/Library/LaunchAgents/com.user.keychain-env.plist` |
| Bash Profile | `~/.bash_profile` |
| Zsh Profile | `~/.zshrc` |
| Claude Desktop Config | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| AWS Credentials | `~/.aws/credentials` |
| AWS Config | `~/.aws/config` |
| Environment Template | `~/.env.example` |
| LaunchAgent Logs | `/tmp/keychain-env.log`, `/tmp/keychain-env.error.log` |

---

## Support

If you encounter issues not covered in this documentation:

1. Check LaunchAgent logs: `/tmp/keychain-env.log`
2. Verify keychain access permissions in Keychain Access app
3. Test manual key retrieval from keychain
4. Restart Claude Desktop after making changes
5. As last resort, restart your Mac

For Claude Desktop specific issues, use `Help → Show Logs` in the application menu.

---

**Last Updated:** $(date)
**Setup Version:** 1.0
