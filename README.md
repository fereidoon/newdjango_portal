# Django & Wagtail CMS Portal

A robust foundation for building content-managed portals using Django and Wagtail CMS.

## Project Structure

```
portal_project/
├── apps/                      # Django applications
│   ├── home/                  # Home app with page models
│   │   ├── migrations/
│   │   ├── templates/home/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   └── apps.py
├── portal/                    # Project configuration
│   ├── settings/
│   │   ├── base.py           # Base settings
│   │   ├── dev.py            # Development settings
│   │   └── prod.py           # Production settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI application
│   └── __init__.py
├── templates/                 # Global templates
│   └── base/
│       └── base.html         # Base template
├── static/                    # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── media/                     # User-uploaded media
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
└── .env.example              # Example environment variables
```

## Features

- **Django 4.2** - Latest stable version
- **Wagtail 5.1** - Enterprise CMS built on Django
- **Page Management** - Create hierarchical pages with rich content
- **Blog System** - Built-in blog index and blog post pages
- **Responsive Templates** - Mobile-friendly design
- **Static Files** - CSS, JavaScript, and image management
- **Media Management** - Wagtail's image and document handling
- **Admin Interface** - Comprehensive Wagtail admin panel
- **Environment Configuration** - Separate settings for development and production

## Installation

### Prerequisites

- Python 3.8+
- pip or conda
- Virtual environment (recommended)

### Setup Steps

1. **Clone or create the project:**
   ```bash
   cd portal_project
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your settings:
   ```
   ENVIRONMENT=development
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server:**
   ```bash
   python manage.py runserver
   ```

   The portal will be available at `http://localhost:8000`
   The admin panel will be at `http://localhost:8000/admin`

## Creating Pages

1. Visit `http://localhost:8000/admin`
2. Navigate to **Pages**
3. Click **Add a page**
4. Choose page type (HomePage, BlogIndexPage, or BlogPage)
5. Fill in content and click **Publish**

## Development

### Creating a New App

```bash
python manage.py startapp app_name apps/app_name
```

### Making Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running Tests

```bash
python manage.py test
```

### Django Shell

```bash
python manage.py shell
```

## Configuration

### Environment Variables

All settings can be controlled via environment variables:

- `ENVIRONMENT` - Set to 'production' for production mode
- `DEBUG` - Set to 'True' or 'False'
- `SECRET_KEY` - Django secret key (change in production!)
- `ALLOWED_HOSTS` - Comma-separated allowed hosts
- `DATABASE_URL` - Database connection string
- `EMAIL_HOST` - SMTP server for sending emails
- `EMAIL_HOST_USER` - Email account username
- `EMAIL_HOST_PASSWORD` - Email account password

### Database Options

The default is SQLite for development. For production, use PostgreSQL:

```
DATABASE_URL=postgresql://user:password@localhost:5432/portal_db
```

Install psycopg2-binary:
```bash
pip install psycopg2-binary
```

## Production Deployment

### Using Gunicorn

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Run with Gunicorn:
   ```bash
   gunicorn portal.wsgi --bind 0.0.0.0:8000 --workers 4
   ```

### Using Docker

Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "portal.wsgi", "--bind", "0.0.0.0:8000"]
```

Build and run:
```bash
docker build -t portal:latest .
docker run -p 8000:8000 portal:latest
```

## Extending the Portal

### Adding Custom Models

1. Create models in `apps/your_app/models.py`
2. Register in `apps.py`
3. Create admin configuration if needed
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Customizing Templates

1. Copy base templates to your app's template directory
2. Extend `base/base.html` in your templates
3. Override blocks as needed

### Adding Custom CSS/JS

1. Add files to `static/css/` or `static/js/`
2. Reference in templates using `{% load static %}`
3. Include in your HTML with `{% static 'css/yourfile.css' %}`

## Useful Commands

```bash
# Create superuser
python manage.py createsuperuser

# Add another superuser
python manage.py createsuperuser

# Check for issues
python manage.py check

# Run database migrations
python manage.py migrate

# Create new migrations
python manage.py makemigrations app_name

# View all migrations
python manage.py showmigrations

# Reverse migrations
python manage.py migrate app_name zero

# Access Django shell
python manage.py shell

# Analyze code
python manage.py check --deploy
```

## Troubleshooting

### Database errors after migration

Reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Static files not loading

Collect static files again:
```bash
python manage.py collectstatic --clear --noinput
```

### Cannot login to admin

Create a new superuser:
```bash
python manage.py createsuperuser
```

## Security Checklist for Production

- [ ] Change `SECRET_KEY` in `.env`
- [ ] Set `DEBUG=False`
- [ ] Set `ENVIRONMENT=production`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use HTTPS (SSL certificate)
- [ ] Set secure database password
- [ ] Configure email settings
- [ ] Review security headers in `settings/prod.py`
- [ ] Enable CSRF and CORS properly
- [ ] Use environment-specific secrets

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Wagtail Documentation](https://docs.wagtail.io/)
- [Wagtail Community](https://wagtail.io/community/)

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please refer to the Django and Wagtail documentation.

---

**Happy coding!** 🚀
