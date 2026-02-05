"""
Management command to create sample gallery with images
"""
from django.core.management.base import BaseCommand
from django.db import connection
from wagtail.models import Page
from apps.home.models import GalleryPage, GalleryImage
from datetime import datetime
import uuid


class Command(BaseCommand):
    help = 'Create a sample gallery page with images'

    def handle(self, *args, **options):
        # Get root page
        root_page = Page.objects.get(depth=1)

        # Create Gallery Page via SQL
        with connection.cursor() as cursor:
            from django.contrib.contenttypes.models import ContentType
            
            gallery_ct = ContentType.objects.get(app_label='home', model='gallerypage')
            
            cursor.execute("""
                INSERT INTO wagtailcore_page 
                (path, depth, numchild, title, slug, draft_title, live, has_unpublished_changes, 
                 url_path, content_type_id, locked, expired, first_published_at, last_published_at, 
                 locale_id, translation_key, show_in_menus, search_description, seo_title)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, ('00010003', 2, 0, 'گالری', 'gallery', 'گالری', 1, 0, '/gallery/', 
                  gallery_ct.id, 0, 0, datetime.now(), datetime.now(), 1, str(uuid.uuid4()), 1, '', ''))
            
            cursor.execute("UPDATE wagtailcore_page SET numchild = 3 WHERE id = 1")

        # Get the created gallery page
        gallery_page = Page.objects.get(slug='gallery')
        
        # Update gallery page intro and description
        GalleryPage.objects.filter(pk=gallery_page.pk).update(
            intro='<p>گالری عکس های حرفه ای ما را مشاهده کنید</p>',
            description='<p>این گالری شامل تصاویر با کیفیت بالا از پروژه های ما و فعالیت های روزمره است. برای دیدن تصاویر با اندازه بزرگ، روی هر تصویر کلیک کنید.</p>'
        )

        self.stdout.write(
            self.style.SUCCESS('✅ Gallery page created successfully at /gallery/')
        )
