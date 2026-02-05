# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. **Navigate to the Project**
```bash
cd portal_project
```

### 2. **Run Setup Script**

**On Linux/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

**On Windows:**
```cmd
setup.bat
```

This script will:
- Create a Python virtual environment
- Install all dependencies
- Set up the database
- Collect static files
- Prompt you to create a superuser account

### 3. **Start the Development Server**
```bash
python manage.py runserver
```

### 4. **Access the Portal**
- **Homepage**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin/
- **Documents**: http://localhost:8000/documents/

### 5. **Create Your First Page**
1. Log in to the admin panel
2. Go to **Pages**
3. Click the **Home** page
4. Click **Add a page**
5. Select **Home Page** as the type
6. Fill in the title and content
7. Click **Publish**

## 📁 Project Structure Overview

```
portal_project/
├── apps/home/              # Home application with page models
├── portal/                 # Project configuration
│   ├── settings/base.py    # Base Django settings
│   ├── settings/dev.py     # Development settings
│   ├── settings/prod.py    # Production settings
│   └── urls.py             # URL routing
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript, images
├── media/                  # User-uploaded files
├── manage.py               # Django management script
└── requirements.txt        # Python packages
```

## 🛠️ Common Commands

### Database
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Admin User
```bash
# Create a superuser
python manage.py createsuperuser

# Delete a superuser
python manage.py shell
# >>> from django.contrib.auth.models import User
# >>> User.objects.get(username='username').delete()
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic

# Clear and recollect
python manage.py collectstatic --clear --noinput
```

### Server
```bash
# Run development server on default port
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000
```

## 🎨 Customization

### Add Custom CSS
Edit `static/css/style.css` or create new CSS files

### Add Custom JavaScript
Edit `static/js/main.js` or create new JS files

### Modify Templates
Edit templates in the `templates/` directory

### Create New App
```bash
python manage.py startapp app_name apps/app_name
```

## 🔧 Configuration

Edit `.env` file to configure:
- `DEBUG` - Development mode (True/False)
- `SECRET_KEY` - Django security key
- `ALLOWED_HOSTS` - Allowed domain names
- `DATABASE_URL` - Database connection

## 📚 Documentation

- [Django Documentation](https://docs.djangoproject.com/)
- [Wagtail Documentation](https://docs.wagtail.io/)
- [Project README](README.md)

## ⚠️ Troubleshooting

### Port 8000 Already in Use
```bash
python manage.py runserver 8080
```

### Database Issues
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

### Can't Access Admin
Reset superuser or create a new one:
```bash
python manage.py createsuperuser
```

## 🚀 Next Steps

1. Customize the templates
2. Add custom CSS and JavaScript
3. Create new pages and content
4. Set up email configuration
5. Configure for production deployment

---

**Happy building!** 🎉
