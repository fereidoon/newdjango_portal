"""
Views for the home app.
"""

from django.shortcuts import render
from wagtail.models import Page

from .models import AnnouncementPage, NewsPage


def home(request):
    """
    Home page view.
    """
    try:
        home_page = Page.objects.get(depth=2).specific
    except Page.DoesNotExist:
        home_page = None
    
    news_items = NewsPage.objects.live().order_by('-first_published_at')[:3]
    announcement_items = AnnouncementPage.objects.live().order_by('-first_published_at')[:3]

    return render(request, 'home/home.html', {
        'page': home_page,
        'news_items': news_items,
        'announcement_items': announcement_items,
    })
