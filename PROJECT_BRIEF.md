# Project Brief: U.S.S. Hamilton LCARS Database

## Project Overview
A Jekyll-based static website serving as a homepage/database for a Star Trek Adventures 2E tabletop RPG campaign featuring the U.S.S. Hamilton. The site uses an LCARS (Library Computer Access and Retrieval System) interface theme inspired by Star Trek: The Next Generation / Picard-era design.

## Technology Stack

### Core Technologies
- **Jekyll**: Static site generator (Ruby-based)
- **GitHub Pages**: Hosting and deployment platform
- **Docker**: Local development environment (Ruby 3.2.2-slim-bullseye base image)
- **Python 3**: Data processing scripts for CSV to JSON conversion

### Frontend
- **jQuery 3.7.0**: JavaScript library for DOM manipulation
- **Showdown.js**: Markdown to HTML converter
- **CSS3**: Custom LCARS styling with multiple theme variants

### Data Sources
- **Google Sheets**: Source of truth for crew data (published as CSV)
- **CSV Files**: Local backup of player character data
- **JSON**: Processed data files consumed by Jekyll templates

## Project Structure

```
├── _data/                    # Jekyll data files (JSON, generated)
├── _includes/                # Jekyll reusable components
│   └── footer-wrapper.html   # Site footer with copyright
├── _layouts/                 # Jekyll page templates
│   ├── default.html          # Standard LCARS layout
│   ├── table_layout.html     # Layout for data tables
│   ├── personal_log.html     # Character personal log layout
│   ├── ship_entry.html       # Ship database entry layout
│   └── species_entry.html    # Species database entry layout
├── assets/                   # Static assets
│   ├── lcars-*.css          # LCARS theme stylesheets
│   ├── lcars.js             # Site JavaScript
│   ├── jquery-3-7-0.min.js  # jQuery library
│   ├── showdown.min.js      # Markdown parser
│   ├── lcars-24.js          # Additional LCARS functionality
│   └── sfcmd.png            # Starfleet Command logo
├── pages/                    # Content pages
│   ├── personal_logs/       # Character personal log entries
│   └── ship_database/       # Ship database entries
├── personal_log_pdfs/        # PDF storage (gitignored)
├── csv_to_json.py           # Fetches senior officers from Google Sheets
├── filter_crew.py           # Fetches and filters crew manifest
├── docker-compose.yml       # Docker development setup
├── Dockerfile               # Jekyll build container
└── .github/workflows/       # CI/CD for GitHub Pages

```

## LCARS Design System

### CSS Theme Variants
- **lcars-ultra-picard.css**: Picard-era theme (primary)
- **lcars-ultra-classic.css**: Classic TNG theme
- **lcars-ultra-nemesis-blue.css**: Nemesis blue variant
- **lcars-colors.css**: Color definitions and utilities

### Color Palette (LCARS Standard)
- Space White: `#f5f6fa`
- Violet Creme: `#dbf`
- Magenta: `#c49`
- Green: `#3c9`
- Blue: `#45f`
- And additional LCARS colors...

### Typography
- **Primary Font**: Antonio (Regular and Bold weights)
- **Font Files**: WOFF2 and WOFF formats in `/assets/`

### Layout Components
- `panel-1` through `panel-8`: Navigation panel IDs
- `bar-1` through `bar-10`: Decorative bar elements
- `top-wrapper`: Header section with navigation
- `left-frame`: Sidebar navigation
- `right-frame`: Main content area
- `footer-wrapper`: Site footer

## Jekyll Configuration

### Front Matter Variables
Common variables used across pages:
- `layout`: Template to use (default, table_layout, personal_log, etc.)
- `title`: Page title
- `lang`: Language code (e.g., "de" for German)
- `back_link`: Back navigation URL
- `heading`: LCARS header text
- `panel_id`: Custom panel identifier (e.g., "SF-557")
- `footer_panel`: Footer panel code (e.g., "XR-47")
- `portrait_icon`: Path to character portrait (personal logs)

### Data Files (Generated)
- `_data/senior_officers.json`: Senior officer roster from Google Sheets
- `_data/crew_manifest.json`: Full crew manifest (filtered for USS Hamilton)

## Data Pipeline

### Google Sheets Integration
1. **Senior Officers**: CSV published from Google Sheets → `csv_to_json.py` → `_data/senior_officers.json`
2. **Crew Manifest**: CSV published from Google Sheets → `filter_crew.py` → `_data/crew_manifest.json`

### Python Scripts
- **csv_to_json.py**: Downloads CSV, converts to JSON, cleans data
- **filter_crew.py**: Downloads CSV, filters for "USS Hamilton Crew", converts to JSON

### Build Process (GitHub Actions)
1. Checkout repository
2. Setup GitHub Pages
3. Install Python and dependencies (`requests`)
4. Run data processing scripts
5. Build with Jekyll
6. Deploy to GitHub Pages

## Development Workflow

### Local Development
```bash
# Using Docker
docker-compose up

# Or using Jekyll directly (requires Ruby)
jekyll serve
```

### Adding Content

#### New Ship Database Entry
1. Create HTML file in `pages/ship_database/`
2. Use front matter:
   ```yaml
   ---
   layout: ship_entry
   title: Ship Name
   lang: de
   back_link: ship_database.html
   heading: SHIP NAME
   ---
   ```

#### New Personal Log
1. Create HTML file in `pages/personal_logs/`
2. Use front matter:
   ```yaml
   ---
   layout: personal_log
   title: Character Name - Log
   back_link: /ship_database.html
   heading: PERSONAL LOG
   portrait_icon: /assets/portraits/character.png
   ---
   ```
3. Add stardate headings with format: `### STARDATE XXXXX.X`

#### New Data Source
1. Update Google Sheets with new data
2. Ensure sheet is published to web as CSV
3. Update Python script URL if needed
4. Run script to generate JSON
5. Reference in templates via `site.data.filename`

## Content Types

### Ship Database
- Ship entries with specifications
- System reports
- Database entries for encountered vessels

### Crew Information
- Senior officers table (dynamically generated from Google Sheets)
- Crew manifest table (filtered from Google Sheets)
- Character personal logs with stardate navigation

### Ship Status
- Current ship sheet (linked PDF)
- Mission logs

## Key URLs and References
- **Live Site**: GitHub Pages deployment
- **Google Sheets**: Source data for crew information
- **LCARS Template**: Based on www.TheLCARS.com template
- **Star Trek IP**: CBS Studios Inc. / Paramount Pictures (fan-made, non-commercial)

## Code Style Guidelines

### Python
- Standard library imports first, then third-party
- Use snake_case for functions and variables
- Include type hints where appropriate
- Handle errors explicitly

### HTML/Jekyll
- Use Liquid templating for dynamic content
- Include fallback values: `{% if page.var %}{{ page.var }}{% else %}default{% endif %}`
- Use `relative_url` filter for asset paths
- Indent with tabs (as per existing codebase)

### CSS
- Follow existing LCARS class naming conventions
- Color classes: `.color-name` for background, `.go-color-name` for text
- Use `!important` for LCARS color overrides
- Maintain LCARS aesthetic: rounded corners, colored panels, futuristic fonts

## Important Notes

### Fan Content Disclaimer
This is a non-commercial fan-made display for a tabletop RPG campaign. Star Trek and all related marks, logos and characters are owned by CBS Studios Inc. No commercial exhibition or distribution is permitted.

### Data Persistence
- Data in `_data/` is generated, not manually edited
- PDFs in `personal_log_pdfs/` are gitignored
- Google Sheets is the source of truth for crew data

### Theme Consistency
- Primary theme: Picard-era LCARS (lcars-ultra-picard.css)
- Language: German ("de") for navigation elements
- Maintains Star Trek "in-universe" feel

---

*Last Updated: February 2026*
