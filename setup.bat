@echo off
REM Portal Project Setup Script for Windows
REM This script sets up the Django and Wagtail CMS portal for development

echo ==================================
echo Portal Project Setup
echo ==================================
echo.

REM Check Python version
echo Checking Python installation...
python --version
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip setuptools wheel >nul 2>&1
echo Pip upgraded
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo Dependencies installed
echo.

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    copy .env.example .env
    echo .env file created
    echo Please edit .env with your configuration
    echo.
)

REM Run migrations
echo Running database migrations...
python manage.py migrate
echo Migrations completed
echo.

REM Create superuser prompt
echo Creating superuser account...
python manage.py createsuperuser
echo.

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput >nul 2>&1
echo Static files collected
echo.

echo ==================================
echo Setup Complete!
echo ==================================
echo.
echo Next steps:
echo 1. Start the development server:
echo    python manage.py runserver
echo.
echo 2. Access the portal:
echo    http://localhost:8000
echo.
echo 3. Access the admin panel:
echo    http://localhost:8000/admin/
echo.
echo 4. Create your first page:
echo    - Go to /admin/pages
echo    - Click 'Add a page'
echo    - Choose HomePage
echo    - Fill content and publish
echo.
pause
