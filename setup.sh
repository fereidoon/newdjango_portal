#!/bin/bash

# Portal Project Setup Script
# This script sets up the Django and Wagtail CMS portal for development

set -e  # Exit on error

echo "=================================="
echo "Portal Project Setup"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python installation..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "✓ Pip upgraded"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "✓ .env file created"
    echo "  Please edit .env with your configuration"
    echo ""
fi

# Run migrations
echo "Running database migrations..."
python manage.py migrate
echo "✓ Migrations completed"
echo ""

# Create superuser prompt
echo "Creating superuser account..."
python manage.py createsuperuser
echo ""

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput > /dev/null 2>&1
echo "✓ Static files collected"
echo ""

echo "=================================="
echo "✓ Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Start the development server:"
echo "   python manage.py runserver"
echo ""
echo "2. Access the portal:"
echo "   http://localhost:8000"
echo ""
echo "3. Access the admin panel:"
echo "   http://localhost:8000/admin/"
echo ""
echo "4. Create your first page:"
echo "   - Go to /admin/pages"
echo "   - Click 'Add a page'"
echo "   - Choose HomePage"
echo "   - Fill content and publish"
echo ""
