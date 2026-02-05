# Portal Project - Development Instructions

This file provides workspace-specific guidance for developing the Django and Wagtail CMS Portal.

## Project Overview

The Portal is a Django project built with Wagtail CMS, providing a solid foundation for content-managed websites.

## Development Setup

1. Navigate to the `portal_project` directory
2. Create and activate a Python virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and configure
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Start development server: `python manage.py runserver`

## Project Structure

- `/apps` - Django applications (home app included)
- `/portal` - Core project configuration
- `/templates` - Global HTML templates
- `/static` - CSS, JavaScript, images
- `/media` - User-uploaded content
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies

## Key Features

- **Wagtail CMS** - Full-featured page management system
- **Page Hierarchy** - Create nested page structures
- **Blog System** - Built-in blog functionality
- **Admin Interface** - Comprehensive Wagtail admin
- **Responsive Design** - Mobile-friendly layouts
- **Media Management** - Image and document handling

## Common Tasks

### Create a New Page
1. Go to `/admin/`
2. Navigate to "Pages"
3. Click "Add a page"
4. Select page type (HomePage, BlogPage, etc.)
5. Fill content and publish

### Create a New App
```bash
python manage.py startapp app_name apps/app_name
```

### Database Migrations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

## Environment Variables

Configure in `.env` file:
- `ENVIRONMENT` - development or production
- `DEBUG` - True or False
- `SECRET_KEY` - Django secret key
- `ALLOWED_HOSTS` - Comma-separated hosts
- `DATABASE_URL` - Database connection string

## Running the Development Server

```bash
python manage.py runserver
```

Access at: http://localhost:8000
Admin at: http://localhost:8000/admin/

## Configuration Files

- `portal/settings/base.py` - Base settings
- `portal/settings/dev.py` - Development settings
- `portal/settings/prod.py` - Production settings
- `portal/urls.py` - URL routing
- `apps/home/models.py` - Page models

## Next Steps

1. Customize templates in `/templates`
2. Add custom JavaScript in `/static/js`
3. Style with CSS in `/static/css`
4. Create new apps as needed
5. Configure email settings for production
6. Set up database (PostgreSQL recommended for production)
7. Configure static files serving (WhiteNoise or web server)

## Useful Documentation

- [Django Docs](https://docs.djangoproject.com/)
- [Wagtail Docs](https://docs.wagtail.io/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## Debugging

- Check logs: `tail -f logs/portal.log` (production)
- Django shell: `python manage.py shell`
- Database inspection: `python manage.py dbshell`
- Run checks: `python manage.py check`

## Production Checklist

- [ ] Update SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up PostgreSQL database
- [ ] Configure email backend
- [ ] Set up HTTPS/SSL
- [ ] Configure logging
- [ ] Collect static files
- [ ] Set secure cookies
- [ ] Enable security headers
