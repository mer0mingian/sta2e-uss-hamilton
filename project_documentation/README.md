# Project Documentation Index

## Overview
This folder contains planning and implementation documentation for the Discord-to-Jekyll automation system for the USS Hamilton RPG website.

## Selected Approach
**Option 2: Custom Discord Bot** - Full self-hosted Python solution with no external service dependencies (n8n, Make.com, etc.)

## Files

### automation-options.md
Summary of all considered automation approaches:
- Option 1: No-code solutions (n8n, Make.com, Zapier) - **REJECTED**
- Option 2: Custom Discord Bot - **SELECTED**
- Option 3: Webhook Relay - **REJECTED**

### implementation-plan.md
Detailed technical specification including:
- Technology stack
- Architecture design
- Module breakdown
- Data flow diagrams
- Deployment options
- Development phases

### requirements.md
Complete requirements specification:
- Functional requirements (FR-001 through FR-008)
- Non-functional requirements (NFR-001 through NFR-004)
- Data models (Pydantic schemas)
- Discord command specifications
- Error handling matrix
- Configuration schema

### checklist.md
Implementation tracking:
- Pre-development setup
- Phase-by-phase development tasks
- Testing checkpoints
- Deployment steps
- Success criteria

### manual-setup-steps.md
Prerequisites for bot implementation:
- Discord Developer Portal setup
- GitHub Personal Access Token generation
- Anthropic API key setup
- Infrastructure/hosting decisions
- Secure credential sharing guidelines

### troubleshooting.md
Common issues and solutions:
- Discord Private Bot / OAuth2 errors
- Intent configuration issues
- OAuth2 scope problems
- Quick reference for correct settings

## Quick Links

- **Main Project**: `/home/mer0/repositories/sta2e-uss-hamilton/`
- **Jekyll Site**: Root of repository
- **Python Scripts**: `csv_to_json.py`, `filter_crew.py`
- **Layouts**: `_layouts/` directory

## Status

**Current Phase**: Awaiting User Setup  
**Next Step**: Complete manual setup steps (see manual-setup-steps.md)  
**Decision**: Proceed with Option 2 - Custom Discord Bot

## Action Required

Please complete the steps in **manual-setup-steps.md** to obtain:
1. Discord Bot Token
2. Discord Server & Channel IDs  
3. GitHub Personal Access Token
4. Anthropic API Key
5. Hosting decision

Once complete, share credentials securely and I'll begin implementation.

## Contact/Notes

This documentation is for internal development reference.  
Created: February 2026  
Selected Approach: Self-hosted Python bot (no external dependencies)
