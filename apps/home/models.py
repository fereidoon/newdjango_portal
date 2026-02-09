"""
Models for the home app.
"""

from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager


class HomePage(Page):
    """
    Home page model.
    This is the main page of the website.
    """
    
    intro = RichTextField(blank=True, help_text='Welcome message')
    
    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = [
        'home.AnnouncementIndexPage',
        'home.BlogIndexPage',
        'home.GalleryPage',
        'home.NewsIndexPage',
    ]

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


class NewsIndexPage(Page):
    """
    News index page that lists all news posts.
    """

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    subpage_types = ['home.NewsPage']

    def get_context(self, request):
        context = super().get_context(request)
        context['news_posts'] = self.get_children().live().order_by('-first_published_at')
        return context

    class Meta:
        verbose_name = "News Index Page"
        verbose_name_plural = "News Index Pages"


class NewsPage(Page):
    """
    Individual news post page.
    """

    date = models.DateField("News date", auto_now_add=True)
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

    parent_page_types = ['home.NewsIndexPage']
    subpage_types = []

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News Page"
        verbose_name_plural = "News Pages"


class AnnouncementIndexPage(Page):
    """
    Announcement index page that lists all announcements.
    """

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    subpage_types = ['home.AnnouncementPage']

    def get_context(self, request):
        context = super().get_context(request)
        context['announcement_posts'] = self.get_children().live().order_by('-first_published_at')
        return context

    class Meta:
        verbose_name = "Announcement Index Page"
        verbose_name_plural = "Announcement Index Pages"


class AnnouncementPage(Page):
    """
    Individual announcement page.
    """

    date = models.DateField("Announcement date", auto_now_add=True)
    summary = models.CharField(max_length=250)
    body = RichTextField()

    search_fields = Page.search_fields + [
        index.SearchField('summary'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        FieldPanel('body'),
    ]

    parent_page_types = ['home.AnnouncementIndexPage']
    subpage_types = []

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Announcement Page"
        verbose_name_plural = "Announcement Pages"


class GalleryPage(Page):
    """
    Professional photo gallery page.
    """
    
    intro = RichTextField(blank=True, help_text='Gallery introduction text')
    description = RichTextField(blank=True, help_text='Gallery description')

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('description'),
        InlinePanel('gallery_images', label='Gallery Images'),
    ]

    parent_page_types = ['wagtailcore.Page']
    subpage_types = []

    def get_context(self, request):
        context = super().get_context(request)
        context['gallery_images'] = self.gallery_images.all()
        return context

    class Meta:
        verbose_name = "Gallery Page"
        verbose_name_plural = "Gallery Pages"


class GalleryImage(models.Model):
    """
    Image model for gallery - linked to GalleryPage.
    """
    
    gallery_page = ParentalKey(
        GalleryPage,
        on_delete=models.CASCADE,
        related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(max_length=255, blank=True, help_text='Image title')
    caption = models.CharField(max_length=500, blank=True, help_text='Image caption')
    order = models.PositiveIntegerField(default=0, help_text='Gallery image order')

    panels = [
        FieldPanel('image'),
        FieldPanel('title'),
        FieldPanel('caption'),
        FieldPanel('order'),
    ]

    class Meta:
        ordering = ['order']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.title or f"Image from {self.gallery_page.title}"
