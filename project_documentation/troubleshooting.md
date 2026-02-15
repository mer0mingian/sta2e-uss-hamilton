# Troubleshooting Guide

## Common Issues and Solutions

### Error: "Private Anwendungen können keinen Standardlink zur Autorisierung haben"
**Translation:** "Private applications cannot have a default authorization link"

**Cause:** The Discord application is set to "Private" but you're trying to configure OAuth2 authorization settings.

**Solutions:**

#### Option 1: Make Bot Public (Recommended)
1. Go to your application in [Discord Developer Portal](https://discord.com/developers/applications)
2. Navigate to **"Bot"** section (left sidebar)
3. Find **"Public Bot"** toggle
4. **Enable** it (turn ON)
5. Click **"Save Changes"**

**Why this works:** Public bots can have OAuth2 authorization links, which you need to invite the bot to your server.

**Security Note:** Making it public doesn't mean anyone can add it - you still control the OAuth2 URL and scopes. It just enables the URL generator functionality.

---

#### Option 2: Remove Authorization Link Settings
If you prefer to keep the bot private:
1. Go to **"OAuth2"** → **"URL Generator"**
2. Clear any redirect URIs you've configured
3. Save changes
4. Then you can keep "Public Bot" disabled

**Note:** You'll need to use a different method to get the bot token, but you won't be able to use the URL generator for invites.

---

## Other Common Issues

### Issue: "Cannot have install fields on a private application"
**Same issue as above** - follow Option 1 or Option 2.

### Issue: Cannot enable "Message Content Intent"
**Cause:** This intent requires verification for bots in 100+ servers, but for development/testing it's freely available.

**Solution:**
1. Go to **"Bot"** → **"Privileged Gateway Intents"**
2. Toggle **"MESSAGE CONTENT INTENT"** ON
3. Save changes
4. If prompted about verification, select "Continue without verification" (you only need verification for bots in 100+ servers)

### Issue: OAuth2 URL says "Invalid scope" or doesn't work
**Cause:** Scopes may not be properly selected.

**Solution:**
1. Go to **"OAuth2"** → **"URL Generator"**
2. Under **Scopes**, select:
   - `bot`
   - `applications.commands`
3. Under **Bot Permissions**, select at minimum:
   - Read Messages/View Channels
   - Send Messages
   - Read Message History
4. Copy the generated URL

### Issue: Bot shows as offline after inviting
**Cause:** Bot needs to be running (the code needs to be active).

**Solution:**
- This is expected! The bot will be offline until you actually run the Python bot code.
- After implementation and deployment, it will come online.

### Issue: "Interaction failed" when using slash commands
**Cause:** Discord didn't receive a response within 3 seconds.

**Future Fix:**
- The bot code will need to acknowledge interactions immediately, then process asynchronously
- This will be handled in the implementation

---

## Still Having Issues?

If you encounter problems not listed here:

1. **Take a screenshot** of the error
2. **Note what step** you were on when it occurred
3. **Describe what you were trying to do**
4. Share this information and I can provide specific guidance

## Quick Reference: Correct Discord Settings

### Bot Section
- ✅ **Public Bot**: ON (for OAuth2 URL generator)
- ✅ **MESSAGE CONTENT INTENT**: ON (required to read messages)
- ✅ **SERVER MEMBERS INTENT**: ON (optional but recommended)

### OAuth2 URL Generator
- **Scopes**: `bot`, `applications.commands`
- **Permissions**: Read Messages, Send Messages, Read History, Add Reactions

---

*Last Updated: February 2026*
