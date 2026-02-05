# Portal Architecture & Foundation

## Project Overview

The Django & Wagtail CMS Portal is a comprehensive foundation for building modern, content-managed web applications. It combines Django's powerful web framework with Wagtail's enterprise-grade CMS capabilities.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│         Portal - Django & Wagtail CMS               │
└─────────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
    ┌───▼────┐      ┌──▼───┐       ┌──▼──────┐
    │ Wagtail│      │ Django     │ Admin    │
    │  CMS   │      │Framework   │Interface │
    └────────┘      └────────┘    └──────────┘
        │               │              │
    ┌───▼───────────────▼──────────────▼────┐
    │     Core Applications & Features      │
    ├──────────────────────────────────────┤
    │ • Page Management                    │
    │ • Blog System                        │
    │ • Media Management                   │
    │ • Search Functionality               │
    │ • Document Management                │
    │ • Forms & Collections                │
    │ • Redirects                          │
    └──────────────────────────────────────┘
        │
    ┌───▼─────────────────────┐
    │  Database Layer         │
    ├─────────────────────────┤
    │ • SQLite (Development)  │
    │ • PostgreSQL (Production)
    │ • Django ORM            │
    └─────────────────────────┘
```

## Core Components

### 1. **Project Configuration** (`portal/`)
- **settings/base.py** - Base settings shared across all environments
- **settings/dev.py** - Development-specific settings (SQLite, debug mode)
- **settings/prod.py** - Production-specific settings (security, logging)
- **urls.py** - URL routing configuration
- **wsgi.py** - WSGI application for deployment

### 2. **Home Application** (`apps/home/`)
Provides the foundation page types:

#### Models:
- **HomePage** - Main landing page
- **BlogIndexPage** - Blog listing page
- **BlogPage** - Individual blog post

#### Supporting Files:
- **models.py** - Page models with Wagtail integration
- **views.py** - View handlers
- **admin.py** - Admin customization
- **migrations/** - Database schema versions

### 3. **Templates** (`templates/`)
```
templates/
├── base/
│   └── base.html          # Master template with styling
└── home/
    └── home.html          # Home page template
```

### 4. **Static Assets** (`static/`)
```
static/
├── css/
│   └── style.css          # Primary stylesheet
├── js/
│   └── main.js            # Core JavaScript
└── images/                # Image assets
```

### 5. **Media Management** (`media/`)
User-uploaded files including:
- Images (managed by Wagtail Image model)
- Documents (managed by Wagtail Document model)
- Other media assets

## Key Features

### Page Management
- Hierarchical page structure
- Drag-and-drop reordering
- Rich text editing with Wagtail's editor
- Scheduled publishing
- Page versioning and revisions
- Preview functionality
- Search indexing

### Blog System
- Blog index pages for listing posts
- Individual blog post pages
- Automatic date management
- Featured images support
- Tag support via django-taggit
- Related posts functionality

### Media Management
- Built-in image upload and cropping
- Document management
- Image optimization
- Integration with page content

### Admin Interface
- Wagtail's user-friendly admin
- WYSIWYG editor
- Real-time preview
- Bulk actions
- Custom admin views available

## Technology Stack

### Backend
- **Django 4.2** - Web framework
- **Wagtail 5.1** - CMS platform
- **Python 3.8+** - Programming language
- **Pillow** - Image processing
- **python-slugify** - URL slug generation

### Database
- **SQLite** - Development database (included)
- **PostgreSQL** - Production-ready database

### Deployment
- **Gunicorn** - WSGI HTTP Server
- **WhiteNoise** - Static file serving
- **Docker** - Containerization (optional)

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling
- **JavaScript** - Client-side interactivity
- **Responsive Design** - Mobile-friendly layouts

## Settings Management

### Base Settings (Shared)
```python
# database, installed_apps, middleware, templates
# static files, media files, security basics
```

### Development Settings
```python
# DEBUG = True
# SQLite database
# Console email backend
# Verbose logging
# All hosts allowed
```

### Production Settings
```python
# DEBUG = False
# Environment-based configuration
# PostgreSQL database
# Email backend setup
# Security headers enabled
# HTTPS enforcement
# Logging to files
```

## Environment Variables

All configuration is managed through environment variables:

```
ENVIRONMENT=development          # development or production
DEBUG=True                        # True for development
SECRET_KEY=...                    # Django secret key
ALLOWED_HOSTS=localhost,127.0.0.1  # Allowed domains
DATABASE_URL=sqlite:///db.sqlite3 # Database connection
EMAIL_HOST=...                    # SMTP server
EMAIL_HOST_USER=...              # Email username
EMAIL_HOST_PASSWORD=...          # Email password
```

## Directory Structure

```
portal_project/
├── .github/
│   └── copilot-instructions.md  # Development guide
├── apps/
│   ├── __init__.py
│   └── home/
│       ├── migrations/
│       ├── templates/home/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       └── views.py
├── portal/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── __init__.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── templates/
│   ├── base/
│   │   └── base.html
│   └── home/
│       └── home.html
├── media/
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── QUICKSTART.md
├── README.md
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── setup.bat
└── setup.sh
```

## Request/Response Flow

```
HTTP Request
    │
    ▼
URL Router (portal/urls.py)
    │
    ├─► Wagtail Admin URLs (/admin/)
    │       │
    │       ▼
    │   Admin Views & Templates
    │
    ├─► Django Admin URLs (/django-admin/)
    │       │
    │       ▼
    │   Django Admin Interface
    │
    └─► Wagtail Pages (/)
            │
            ▼
        Page Model (apps/home/models.py)
            │
            ▼
        Page Template (templates/)
            │
            ▼
        Static Assets (static/)
            │
            ▼
        HTTP Response
```

## Data Models

### HomePage
```
- title (inherited from Page)
- intro (RichTextField)
- content_panels (admin configuration)
```

### BlogIndexPage
```
- title (inherited from Page)
- intro (RichTextField)
- get_context() (returns child blog posts)
```

### BlogPage
```
- title (inherited from Page)
- date (DateField, auto-added)
- intro (CharField, max_length=250)
- body (RichTextField)
- search_fields (for indexing)
```

## Development Workflow

1. **Local Development**
   - Use development settings
   - SQLite database
   - Debug mode enabled
   - Hot reload server

2. **Testing**
   - Run tests: `python manage.py test`
   - Check code: `python manage.py check`
   - Database validation: `python manage.py migrate --dry-run`

3. **Staging**
   - Deploy to staging environment
   - Test with production settings
   - Verify database migrations
   - Test email functionality

4. **Production**
   - Use production settings
   - PostgreSQL database
   - Container deployment (Docker)
   - HTTPS enforcement
   - Static files served by web server

## Extensibility

The foundation is designed to be easily extended:

### Add New App
```bash
python manage.py startapp app_name apps/app_name
```

### Add Custom Models
Create in `apps/your_app/models.py` and register in settings

### Add Custom Blocks
Extend Wagtail's StreamBlock with custom blocks

### Add Custom Admin Views
Create custom views in `apps/your_app/views.py`

### Customize Templates
Override base templates in your app's template directory

## Security Features

### Built-in Security
- CSRF protection
- XSS prevention
- SQL injection prevention (via ORM)
- Secure password hashing
- Session security

### Production Security
- HTTPS/SSL support
- Secure cookie flags
- HSTS headers
- CSP headers (configurable)
- Security headers enabled

## Performance Considerations

### Static Files
- WhiteNoise for efficient serving
- CSS/JS minification (production)
- Image optimization with Pillow

### Database
- SQLite for development
- PostgreSQL for production
- Query optimization via Django ORM

### Caching
- Built-in Django caching framework
- Wagtail's caching mechanisms
- HTTP caching headers

## Deployment Options

### Docker
```bash
docker build -t portal:latest .
docker-compose up
```

### Traditional Server
```bash
python manage.py collectstatic
gunicorn portal.wsgi --bind 0.0.0.0:8000
```

### Cloud Platforms
- AWS (Elastic Beanstalk, Lambda)
- Google Cloud (App Engine, Cloud Run)
- Heroku
- DigitalOcean
- Azure App Service

## Next Steps for Development

1. **Customize**
   - Modify templates
   - Add custom CSS/JS
   - Create new page types

2. **Extend**
   - Add new apps
   - Create custom models
   - Implement business logic

3. **Test**
   - Write unit tests
   - Integration tests
   - End-to-end tests

4. **Deploy**
   - Set up production environment
   - Configure database
   - Set up email
   - Deploy application

## Documentation References

- [Django Documentation](https://docs.djangoproject.com/)
- [Wagtail Documentation](https://docs.wagtail.io/)
- [Python Documentation](https://docs.python.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
