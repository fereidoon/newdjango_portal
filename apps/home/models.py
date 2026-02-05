"""
Models for the home app.
"""

from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class HomePage(Page):
    """
    Home page model.
    This is the main page of the website.
    """
    
    intro = RichTextField(blank=True, help_text='Welcome message')
    
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = []

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class BlogIndexPage(Page):
    """
    Blog index page that lists all blog posts.
    """
    
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = ['home.BlogPage']

    def get_context(self, request):
        context = super().get_context(request)
        blog_pages = self.get_children().live().order_by('-first_published_at')
        context['blog_posts'] = blog_pages
        return context

    class Meta:
        verbose_name = "Blog Index Page"


class BlogPage(Page):
    """
    Individual blog post page.
    """
    
    date = models.DateField("Post date", auto_now_add=True)
    intro = models.CharField(max_length=250)
    body = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    parent_page_types = ['home.BlogIndexPage']
    subpage_types = []

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Pages"
