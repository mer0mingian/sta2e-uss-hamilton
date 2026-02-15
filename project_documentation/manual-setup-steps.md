# Manual Setup Steps for Discord Bot Implementation

**Status:** Awaiting user completion  
**Purpose:** Steps required before bot development can begin  
**Approach:** Option 2 - Custom Python Discord Bot (self-hosted)

---

## Overview

Before I can implement the Discord bot, you need to complete several manual setup steps to obtain API keys, tokens, and configure services. This document lists all required actions.

---

## Step 1: Discord Developer Setup

### 1.1 Create Discord Application
1. Navigate to https://discord.com/developers/applications
2. Click **"New Application"**
3. Name it (suggestion: "USS Hamilton Log Bot")
4. Click **"Create"**

### 1.2 Configure Bot Settings
1. In your application, go to the **"Bot"** section (left sidebar)
2. Click **"Reset Token"** (⚠️ You'll only see this once - **SAVE IT SECURELY**)
3. Under **"Privileged Gateway Intents"**, enable:
   - ✅ **MESSAGE CONTENT INTENT** (required to read message content)
   - ✅ **SERVER MEMBERS INTENT** (optional but recommended)
4. Click **"Save Changes"**

### 1.3 Generate Invite URL
1. Go to **"OAuth2"** → **"URL Generator"** (left sidebar)
2. Under **"Scopes"**, select:
   - ✅ **bot**
   - ✅ **applications.commands**
3. Under **"Bot Permissions"**, select:
   - ✅ **Read Messages/View Channels**
   - ✅ **Send Messages**
   - ✅ **Read Message History**
   - ✅ **Add Reactions**
   - ✅ **Use Slash Commands**
   - ✅ **Attach Files** (optional, for testing)
4. Copy the generated URL at the bottom
5. Open the URL in your browser and invite the bot to your server
6. **Authorize** the bot for your server

### 1.4 Get Server ID
1. In Discord, enable **Developer Mode** if not already enabled:
   - User Settings → Advanced → Developer Mode (toggle ON)
2. Right-click your server name in the channel list
3. Click **"Copy Server ID"**
4. **Save this ID**

### 1.5 Get Channel ID
1. Create a test channel/thread for the bot (suggested: `#bot-testing`)
2. Right-click the channel name
3. Click **"Copy Channel ID"**
4. **Save this ID**

**Deliverable from Step 1:**
- Bot Token (keep secret!)
- Server ID
- Channel ID

---

## Step 2: GitHub Setup

### 2.1 Generate Personal Access Token
1. Go to https://github.com/settings/tokens
2. Click **"Generate new token (classic)"**
3. Give it a descriptive name (e.g., "USS Hamilton Discord Bot")
4. Set expiration (recommendation: 90 days for security)
5. Select scopes:
   - ✅ **repo** (Full control of private repositories)
   - ✅ **workflow** (Update GitHub Action workflows - optional)
6. Click **"Generate token"**
7. **SAVE THE TOKEN IMMEDIATELY** (you won't see it again)

### 2.2 Repository Information
Note your repository details:
- Repository name format: `username/repo-name` (e.g., `yourname/sta2e-uss-hamilton`)
- Confirm you have push access to this repository

### 2.3 Decide on Workflow
Choose your preferred approach:
- **Option A:** Direct commits to `main` branch (faster, simpler)
- **Option B:** Create Pull Requests for manual review (safer, recommended)

**Deliverable from Step 2:**
- GitHub Personal Access Token (keep secret!)
- Repository name (owner/repo format)
- Preferred workflow (direct commits or PRs)

---

## Step 3: Anthropic (Claude) API Setup

### 3.1 Get API Access
1. Navigate to https://console.anthropic.com/
2. Sign up for an account or log in
3. Complete any required verification
4. Add a payment method (credit card required, but usage is very cheap - pennies per log)

### 3.2 Generate API Key
1. Go to the API keys section
2. Click **"Create Key"**
3. Give it a name (e.g., "USS Hamilton Bot")
4. **SAVE THE API KEY** (you won't see it again)

**Note:** Claude API pricing is approximately $0.01-0.05 per personal log processed, depending on length. Very cost-effective for this use case.

**Deliverable from Step 3:**
- Anthropic API Key (keep secret!)

---

## Step 4: Infrastructure Decision

### 4.1 Choose Hosting Platform

**Option A - VPS/Cloud Server** (⭐ Recommended)
- **Hetzner:** CX11 instance (~€3.79/month) - https://www.hetzner.com/cloud
- **DigitalOcean:** Basic Droplet ($5/month) - https://www.digitalocean.com
- **AWS:** t3.micro (free tier eligible for 12 months)
- **Existing Server:** If you already have a VPS

**Option B - Local Machine** (for testing only)
- Can run on your computer
- Bot goes offline when computer sleeps
- Good for initial development/testing

**Option C - Raspberry Pi**
- Perfect for low-traffic bots
- Runs 24/7 with minimal power

### 4.2 If Using VPS, Prepare Access
- Create server/account
- Ensure SSH access is working
- Note the server IP address
- Have root or sudo access

**Deliverable from Step 4:**
- Hosting choice
- Server credentials/access (if VPS)

---

## Step 5: Configuration Decisions

### 5.1 Choose Trigger Tag
Decide what hashtag/tag will trigger the bot to process a message:

Suggestions:
- `#personal-log` (explicit)
- `#log` (shorter)
- `#mission-log` (for missions)
- Multiple tags supported if needed

### 5.2 Content Guidelines (Optional)
Consider giving your players guidelines for posting logs:
- Include stardate in format `XXXXX.X`
- Start with character name
- Tag with `#personal-log`
- Attach PDF or write directly in message

**Deliverable from Step 5:**
- Chosen trigger tag(s)
- Any specific content requirements

---

## Summary Checklist

Before I can start implementation, confirm you have:

```
□ Discord Bot Token (from Step 1.2)
□ Discord Server ID (from Step 1.4)
□ Discord Channel ID (from Step 1.5)
□ GitHub Personal Access Token (from Step 2.1)
□ GitHub Repository name (from Step 2.2)
□ Anthropic API Key (from Step 3.2)
□ Hosting decision made (from Step 4)
□ Trigger tag chosen (from Step 5)
□ All credentials saved securely
```

---

## Secure Credential Sharing

When you have completed these steps, you'll need to share the credentials with me. **DO NOT post them in regular chat.**

Options for secure sharing:
1. **Environment file:** Create a `.env` file and share it securely
2. **Private message:** If your platform supports private/DM messages
3. **Temporary paste:** Use a service like https://privnote.com/ (self-destructing)
4. **File attachment:** Save in a file and share directly

I'll need these exact variables:
```bash
DISCORD_BOT_TOKEN=your_token_here
DISCORD_SERVER_ID=your_server_id
DISCORD_CHANNEL_ID=your_channel_id
GITHUB_TOKEN=your_github_token
GITHUB_REPO=username/repo-name
ANTHROPIC_API_KEY=your_anthropic_key
TRIGGER_TAG=your_chosen_tag
```

---

## What Happens Next

Once you confirm completion of these steps:

1. **Share credentials** with me securely
2. **I'll implement** the complete bot code
3. **Local testing** - I'll verify the bot works correctly
4. **Deployment** - We'll deploy to your chosen infrastructure
5. **Testing phase** - Test with sample messages in your test channel
6. **Go live** - Start processing real player logs!

---

## Timeline Estimate

**Your setup time:** 30-60 minutes (depending on familiarity with platforms)

**My implementation time:** 
- Phase 1 (Core Bot): 2-3 hours
- Phase 2 (PDF + LLM): 3-4 hours
- Phase 3 (GitHub integration): 2-3 hours
- Phase 4 (Testing & Polish): 2-3 hours
- **Total: 1-2 days** after receiving credentials

---

## Questions or Issues?

If you encounter problems with any step:
1. Note the specific error or issue
2. Share screenshots if helpful
3. I can provide troubleshooting guidance

**Ready when you are!** Complete the steps above and let me know when you're ready to proceed.

---

*Last Updated: February 2026*  
*Document Version: 1.0*
