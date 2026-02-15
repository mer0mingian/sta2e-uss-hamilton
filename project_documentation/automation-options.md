# Discord-to-Jekyll Automation Options Summary

## Context
Goal: Automatically process Discord messages (text and PDF attachments) containing player personal logs and update the USS Hamilton Jekyll site with structured content.

## Option 1: No-Code/Low-Code Solutions

### n8n / Make.com
**Approach:** Visual workflow builder connecting Discord → PDF processor → LLM → GitHub

**Pros:**
- Visual workflow building
- Built-in error handling
- PDF extraction nodes available
- No coding required

**Cons:**
- Vendor lock-in
- Paid tiers for higher volume
- Less flexibility for custom logic
- Dependency on external service availability

**Verdict:** ❌ REJECTED - User explicitly wants to avoid service dependencies

### Zapier + Webhooks
**Approach:** Zapier triggers on Discord messages, processes through their integrations

**Pros:**
- Well-established platform
- Many integrations

**Cons:**
- Expensive for automation volume
- Limited customization
- Another external dependency

**Verdict:** ❌ REJECTED - Same concerns as n8n/Make.com

---

## Option 2: Custom Discord Bot (SELECTED)

**Approach:** Python-based Discord bot deployed on self-managed infrastructure

### Architecture
```
Discord Channel/Thread
    ↓
Discord Bot (discord.py)
    ↓
PDF Text Extraction (pdfplumber/pymupdf)
    ↓
LLM Structured Extraction (Claude + Instructor)
    ↓
GitHub API (PyGithub)
    ↓
Jekyll Site Update
```

### Pros:
- ✅ **Full control** over logic and data flow
- ✅ **No vendor lock-in** - entirely self-hosted
- ✅ **Customizable** extraction and formatting
- ✅ **Cost-effective** - only pay for hosting and API usage
- ✅ **Local data** - sensitive content never leaves your infrastructure (except LLM API)
- ✅ **Extensible** - can add features as needed

### Cons:
- Requires development effort
- Need to manage hosting/deployment
- Responsible for maintenance

**Verdict:** ✅ SELECTED - Meets requirement of no external service dependencies

---

## Option 3: Webhook Relay Bot

**Approach:** Lightweight Discord bot that forwards events to webhook, processing done elsewhere

**Pros:**
- Simple bot code
- Processing logic separate

**Cons:**
- Still requires webhook endpoint (could be self-hosted)
- Two components to manage
- More complex overall

**Verdict:** ❌ Not needed - Option 2 provides cleaner single-component solution

---

## Decision

**Selected: Option 2 - Custom Discord Bot**

Rationale:
1. User requirement: No dependency on n8n, Make.com, or similar services
2. Full control over data and processing logic
3. Can be hosted on existing infrastructure or cheap VPS
4. One codebase to maintain vs. multiple integrated services
5. Extensible for future requirements

---

## Implementation Notes

See `implementation-plan.md` for detailed technical specification.
