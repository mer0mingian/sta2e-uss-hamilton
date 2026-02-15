# Discord Bot Implementation Plan

## Overview
Custom Python Discord bot to automate processing of player personal logs from Discord to Jekyll site.

## Technology Stack

### Core Dependencies
- **discord.py** or **pycord**: Discord bot framework
- **pdfplumber** or **pymupdf**: PDF text extraction
- **instructor**: Structured LLM output with Pydantic
- **anthropic**: Claude API client
- **PyGithub**: GitHub API integration
- **pydantic**: Data validation and serialization

### Optional/Enhancement
- **aiohttp**: Async HTTP client (if needed)
- **python-dotenv**: Environment variable management
- **loguru**: Better logging
- **pytest**: Testing

## Architecture Components

### 1. Discord Bot Module (`bot/`)
```
bot/
├── __init__.py
├── main.py              # Bot entry point
├── handlers.py          # Message event handlers
├── config.py           # Configuration management
└── utils.py            # Discord-specific utilities
```

**Responsibilities:**
- Connect to Discord Gateway
- Listen for messages in specific channels/threads
- Filter messages by criteria (hashtag, attachment type)
- Download PDF attachments
- Trigger processing pipeline

### 2. PDF Processing Module (`processors/`)
```
processors/
├── __init__.py
├── pdf_extractor.py    # PDF text extraction
└── text_cleaner.py     # Text preprocessing
```

**Responsibilities:**
- Extract text from PDF files
- Handle multi-page documents
- Clean and normalize extracted text
- Error handling for corrupted/encrypted PDFs

### 3. LLM Extraction Module (`extractors/`)
```
extractors/
├── __init__.py
├── schema.py           # Pydantic models for structured data
├── claude_client.py    # Claude API integration
└── prompts.py          # LLM prompts
```

**Responsibilities:**
- Define structured output schemas (Pydantic)
- Send extracted text to Claude
- Parse and validate LLM responses
- Handle extraction failures gracefully

### 4. GitHub Integration Module (`github_integration/`)
```
github_integration/
├── __init__.py
├── client.py           # GitHub API wrapper
├── file_generator.py   # Jekyll file generation
└── templates.py        # HTML/Jekyll templates
```

**Responsibilities:**
- Authenticate with GitHub API
- Generate Jekyll-compatible HTML files
- Create commits or pull requests
- Handle file naming and front matter

### 5. Configuration (`config/`)
```
config/
├── settings.py         # Application settings
└── channels.yaml       # Discord channel mappings
```

## Data Flow

```
1. Player posts in Discord channel
   └── Message contains: text, optional PDF attachment

2. Bot detects message
   └── Filter: specific channel/thread, contains #log tag

3. If PDF attached:
   └── Download → Extract text using pdfplumber

4. Combine text sources
   └── Message content + PDF content (if any)

5. Send to Claude with structured prompt
   └── Schema: PersonalLogEntry (stardate, character, content, etc.)

6. Validate extracted data
   └── Pydantic validation

7. Generate Jekyll file
   └── HTML with YAML front matter

8. Commit to GitHub
   └── Option A: Direct commit to main
   └── Option B: Create PR for review

9. GitHub Actions builds site
   └── Jekyll builds and deploys
```

## File Structure

```
discord-bot/
├── bot/
│   ├── __init__.py
│   ├── main.py
│   ├── handlers.py
│   ├── config.py
│   └── utils.py
├── processors/
│   ├── __init__.py
│   ├── pdf_extractor.py
│   └── text_cleaner.py
├── extractors/
│   ├── __init__.py
│   ├── schema.py
│   ├── claude_client.py
│   └── prompts.py
├── github_integration/
│   ├── __init__.py
│   ├── client.py
│   ├── file_generator.py
│   └── templates.py
├── config/
│   ├── settings.py
│   └── channels.yaml
├── tests/
│   └── (test files)
├── requirements.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Configuration Schema

### Environment Variables (.env)
```bash
# Discord
DISCORD_BOT_TOKEN=your_bot_token_here
DISCORD_GUILD_ID=your_server_id
DISCORD_LOG_CHANNEL_ID=channel_id_to_monitor

# Anthropic
ANTHROPIC_API_KEY=your_claude_api_key

# GitHub
GITHUB_TOKEN=your_github_pat
GITHUB_REPO=username/sta2e-uss-hamilton
GITHUB_BRANCH=main

# Bot Settings
BOT_COMMAND_PREFIX=!
BOT_LOG_LEVEL=INFO
DRY_RUN=false  # Set to true for testing without GitHub commits
```

### Channel Mappings (channels.yaml)
```yaml
channels:
  - id: 123456789
    name: "personal-logs"
    type: "forum"  # or "text", "thread"
    required_tag: "#personal-log"
    template: "personal_log"
    auto_approve: false
    
  - id: 987654321
    name: "mission-reports"
    type: "text"
    required_tag: "#mission"
    template: "mission_log"
    auto_approve: true
```

## Deployment Options

### Option A: VPS/Cloud Server (Recommended)
- **Platform:** Hetzner, DigitalOcean, AWS EC2, or existing server
- **Process Manager:** PM2 or systemd
- **Monitoring:** Basic logging + optional alerting

### Option B: Containerized (Docker)
- **Platform:** Any Docker host
- **Orchestration:** Docker Compose for local, Kubernetes for scale
- **Benefits:** Consistent environment, easy deployment

### Option C: Serverless (Advanced)
- **Platform:** AWS Lambda + API Gateway
- **Trigger:** Discord webhook instead of Gateway connection
- **Pros:** Pay-per-use, auto-scaling
- **Cons:** Cold start latency, more complex setup

## Development Phases

### Phase 1: Core Bot
- [ ] Basic Discord bot connection
- [ ] Message listening and filtering
- [ ] PDF download and text extraction
- [ ] Basic logging

### Phase 2: LLM Integration
- [ ] Claude API client
- [ ] Structured extraction with Pydantic
- [ ] Prompt engineering for log extraction
- [ ] Error handling and retries

### Phase 3: GitHub Integration
- [ ] GitHub API authentication
- [ ] File generation with Jekyll front matter
- [ ] Commit/PR creation
- [ ] Branch management

### Phase 4: Polish
- [ ] Comprehensive error handling
- [ ] User feedback in Discord
- [ ] Admin commands (retry, status, etc.)
- [ ] Testing suite
- [ ] Documentation

## Security Considerations

1. **Token Management**
   - Store all tokens in environment variables
   - Use GitHub Secrets or similar for deployment
   - Rotate tokens regularly

2. **Content Validation**
   - Sanitize all extracted text before saving
   - Validate file paths to prevent directory traversal
   - Size limits on PDFs and messages

3. **Rate Limiting**
   - Respect Discord API rate limits
   - Implement exponential backoff
   - Queue processing for bulk operations

4. **Access Control**
   - Restrict bot to specific channels
   - Validate user permissions before processing
   - Audit log of all actions

## Cost Estimate

| Component | Monthly Cost |
|-----------|--------------|
| VPS (smallest instance) | $5-10 |
| Anthropic Claude API | ~$0.01-0.05 per log |
| GitHub (public repo) | Free |
| **Total** | **~$5-15/month** |

## Next Steps

1. Review and approve implementation plan
2. Set up development environment
3. Create bot application in Discord Developer Portal
4. Generate GitHub Personal Access Token
5. Obtain Anthropic API key
6. Implement Phase 1 (Core Bot)
7. Test with sample data
8. Deploy to production

## Open Questions

1. Should processed logs require manual approval before publishing?
2. How to handle updates to existing logs (edits)?
3. Should the bot support images/other attachments?
4. What validation should be done on extracted stardates?
5. How to handle multi-part logs (series of messages)?
