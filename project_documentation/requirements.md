# Discord Bot Requirements Specification

## Functional Requirements

### FR-001: Message Monitoring
The bot SHALL monitor specific Discord channels and threads for new messages.

**Acceptance Criteria:**
- Bot connects to Discord Gateway successfully
- Listens for `on_message` events
- Can filter by channel ID and/or category

### FR-002: Tag-Based Filtering
The bot SHALL only process messages containing specific trigger tags.

**Acceptance Criteria:**
- Recognizes tags like `#personal-log`, `#log`, `#mission-report`
- Case-insensitive matching
- Tag can appear anywhere in message

### FR-003: PDF Attachment Handling
The bot SHALL download and extract text from PDF attachments.

**Acceptance Criteria:**
- Download PDFs up to 25MB (Discord limit)
- Extract text using pdfplumber or pymupdf
- Handle multi-page PDFs
- Clean up temporary files after processing

### FR-004: Text Message Handling
The bot SHALL process plain text messages as personal logs.

**Acceptance Criteria:**
- Extract message content
- Support Discord markdown formatting
- Preserve line breaks and structure

### FR-005: Structured Data Extraction
The bot SHALL use an LLM to extract structured data from log content.

**Required Fields:**
- Character name
- Stardate (format: XXXXX.X)
- Log title/subject
- Log content (formatted text)
- Tags/categories (optional)

**Acceptance Criteria:**
- Uses Claude 3.5 Sonnet or better
- Returns valid JSON matching schema
- Handles incomplete/missing data gracefully

### FR-006: Jekyll File Generation
The bot SHALL generate valid Jekyll HTML files.

**Acceptance Criteria:**
- Includes YAML front matter
- Uses appropriate layout template
- Valid HTML content
- Proper file naming convention

### FR-007: GitHub Integration
The bot SHALL create or update files in the GitHub repository.

**Acceptance Criteria:**
- Authenticates with GitHub API
- Creates files in `pages/personal_logs/`
- Generates unique filenames based on stardate/character
- Creates meaningful commit messages

### FR-008: User Feedback
The bot SHALL provide feedback in Discord about processing status.

**Acceptance Criteria:**
- Reacts to message with ⏳ while processing
- Reacts with ✅ on success
- Reacts with ❌ on failure
- Sends detailed error message in thread on failure

## Non-Functional Requirements

### NFR-001: Reliability
The bot SHALL handle errors gracefully and continue operating.

**Criteria:**
- 99% uptime target
- Automatic restart on crash
- Error logging to file

### NFR-002: Performance
The bot SHALL process messages within reasonable time.

**Criteria:**
- PDF download: < 5 seconds
- Text extraction: < 10 seconds
- LLM processing: < 30 seconds
- GitHub commit: < 10 seconds
- Total: < 60 seconds for typical log

### NFR-003: Security
The bot SHALL handle sensitive data securely.

**Criteria:**
- No tokens in code
- Secure temp file handling
- No logging of sensitive content
- Rate limiting compliance

### NFR-004: Scalability
The bot SHALL handle multiple concurrent requests.

**Criteria:**
- Async processing
- Queue for LLM requests
- Configurable concurrency limits

## Data Models

### PersonalLogEntry (Pydantic Model)
```python
class PersonalLogEntry(BaseModel):
    character_name: str = Field(..., description="Name of the character")
    stardate: str = Field(..., pattern=r"^\d{5}\.\d$", description="Stardate in format XXXXX.X")
    title: str = Field(..., max_length=200, description="Log title/subject")
    content: str = Field(..., description="Main log content in markdown")
    location: Optional[str] = Field(None, description="Location mentioned in log")
    tags: List[str] = Field(default_factory=list, description="Additional tags")
    is_canon: bool = Field(True, description="Whether this is canon content")
```

### ProcessingResult
```python
class ProcessingResult(BaseModel):
    success: bool
    message_id: str
    channel_id: str
    github_url: Optional[str]
    error_message: Optional[str]
    processing_time_ms: int
```

## Discord Command Requirements

### Admin Commands (Slash Commands)

#### `/status`
Show bot status and statistics

#### `/retry <message_id>`
Manually retry processing a specific message

#### `/config`
View current configuration

#### `/test <message_link>`
Test process a message without committing to GitHub (dry run)

### Public Commands

None required - bot operates automatically on tagged messages.

## Error Handling Requirements

### Error Types and Responses

| Error | User Response | Admin Alert | Retry |
|-------|--------------|-------------|-------|
| PDF too large | ❌ + message "PDF exceeds size limit" | Log | No |
| PDF corrupted | ❌ + message "Unable to read PDF" | Log | Manual |
| LLM timeout | ❌ + message "Processing timeout, please retry" | Alert | Yes |
| GitHub API error | ❌ + message "Unable to save log" | Alert | Yes |
| Missing required field | ❌ + message "Log missing required info (stardate)" | Log | Manual |
| Rate limited | ⏳ + message "Rate limited, will retry..." | Log | Auto |

## Configuration Requirements

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| DISCORD_BOT_TOKEN | Yes | Discord bot authentication token |
| DISCORD_GUILD_ID | Yes | Server ID to monitor |
| ANTHROPIC_API_KEY | Yes | Claude API key |
| GITHUB_TOKEN | Yes | GitHub Personal Access Token |
| GITHUB_REPO | Yes | Repository name (owner/repo) |
| LOG_LEVEL | No | Logging level (default: INFO) |
| DRY_RUN | No | Test mode without GitHub commits |
| MAX_PDF_SIZE_MB | No | PDF size limit (default: 25) |

### Channel Configuration

```yaml
monitored_channels:
  - channel_id: "123456789"
    channel_name: "personal-logs"
    channel_type: "forum"  # forum, text, announcement
    trigger_tags: ["#personal-log", "#log"]
    template: "personal_log"
    auto_publish: false
    require_approval: true
```

## Testing Requirements

### Unit Tests
- PDF extraction with various PDF types
- LLM extraction with sample texts
- GitHub API mocking
- Configuration validation

### Integration Tests
- Discord connection (test server)
- End-to-end message processing
- Error scenario handling

### Sample Data
- Valid personal log text
- PDF with formatted log
- Multi-part Discord message
- Edge cases (empty content, missing stardate, etc.)

## Deployment Requirements

### Production Deployment
- Docker containerization
- Environment-based configuration
- Health check endpoint
- Log rotation
- Process monitoring (PM2/systemd)

### Development Setup
- Local Discord test server
- GitHub test repository
- Sample PDFs and messages
- Debug logging enabled

## Future Enhancements (Out of Scope for V1)

- Support for images in logs (extract and save to assets)
- Edit detection and log updates
- Multi-language support
- Advanced approval workflow with web UI
- Statistics dashboard
- Automatic stardate validation
- Log series/chapter linking
- Search index updates
