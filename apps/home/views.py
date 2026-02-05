"""
Views for the home app.
"""

from django.shortcuts import render
from wagtail.models import Page


def home(request):
    """
    Home page view.
    """
    try:
        home_page = Page.objects.get(depth=2).specific
    except Page.DoesNotExist:
        home_page = None
    
    return render(request, 'home/home.html', {
        'page': home_page,
    })
