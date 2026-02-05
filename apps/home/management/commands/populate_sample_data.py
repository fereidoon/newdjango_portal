"""
Django management command to populate database with sample Persian content
Run with: python manage.py populate_sample_data
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page
from apps.home.models import HomePage, BlogIndexPage, BlogPage


class Command(BaseCommand):
    help = 'Populate database with sample Persian content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Starting to populate sample data...'))
        
        # Get the root page
        try:
            root_page = Page.objects.get(depth=1)
        except Page.DoesNotExist:
            self.stdout.write(self.style.ERROR('❌ Root page not found!'))
            return
        
        # Create Home Page if it doesn't exist
        if not HomePage.objects.exists():
            home_page = root_page.add_child(instance=HomePage(
                title="صفحه اصلی",
                slug="home",
                intro="<p>خوش آمدید به پورتال ما! این یک مرکز مدیریت محتوا است که بر پایه Django و Wagtail بنا شده است.</p>",
                live=True
            ))
            self.stdout.write(self.style.SUCCESS(f'✓ Home page created: {home_page.title}'))
        else:
            home_page = HomePage.objects.first()
            self.stdout.write(self.style.WARNING(f'✓ Home page already exists: {home_page.title}'))
        
        # Create Blog Index Page if it doesn't exist
        if not BlogIndexPage.objects.exists():
            blog_index = root_page.add_child(instance=BlogIndexPage(
                title="وبلاگ",
                slug="blog",
                intro="<p>آخرین مقالات و نوشته های ما را اینجا بخوانید.</p>",
                live=True
            ))
            self.stdout.write(self.style.SUCCESS(f'✓ Blog index page created: {blog_index.title}'))
        else:
            blog_index = BlogIndexPage.objects.first()
            self.stdout.write(self.style.WARNING(f'✓ Blog index page already exists: {blog_index.title}'))
        
        # Sample blog posts data
        sample_posts = [
            {
                "title": "آغاز یک سفر جدید به دنیای وب",
                "intro": "در این مقاله، ما درباره آخرین تکنولوژی‌های وب صحبت خواهیم کرد.",
                "body": "<h2>مقدمه</h2><p>وب با سرعت زیادی درحال تکامل است. هر روز تکنولوژی‌های جدیدی معرفی می‌شوند که به ما کمک می‌کنند بهتر کار کنیم.</p><h2>اهمیت Django</h2><p>Django یکی از بهترین فریم‌ورک‌های Python برای توسعه وب است. این فریم‌ورک به ما کمک می‌کند تا وبلاگ‌های امن و مقیاس‌پذیر بسازیم.</p>"
            },
            {
                "title": "محتوای بهتر با Wagtail CMS",
                "intro": "Wagtail یکی از بهترین سیستم‌های مدیریت محتوا برای Django است.",
                "body": "<h2>چرا Wagtail؟</h2><p>Wagtail بسیار قدرتمند است و استفاده از آن بسیار آسان. شما می‌توانید صفحات پیچیده‌ای را بدون نوشتن کد بیشتر درست کنید.</p><p>یکی دیگر از مزایای Wagtail، واسط کاربری آن است که بسیار کاربرپسند است.</p>"
            },
            {
                "title": "طراحی شامل و مناسب برای تمام برنامه‌ها",
                "intro": "در عصر دیجیتالی، داشتن یک وب‌سایت پاسخگو بسیار ضروری است.",
                "body": "<h2>اهمیت طراحی واکنش‌پذیر</h2><p>امروزه، اکثر کاربران از تلفن‌های هوشمند برای دسترسی به وب‌سایت‌ها استفاده می‌کنند. بنابراین، داشتن یک طراحی واکنش‌پذیر ضروری است.</p><p>ما در این پروژه، Bootstrap 5 را استفاده کردیم.</p>"
            },
            {
                "title": "پشتیبانی کامل فارسی و RTL",
                "intro": "یکی از ویژگی‌های خاص این پرژه، پشتیبانی کامل زبان فارسی است.",
                "body": "<h2>چرا فارسی؟</h2><p>فارسی یکی از زبان‌های مهم است. و این پروژه به طور کامل برای استفاده با زبان فارسی طراحی شده است.</p><h2>RTL چیست؟</h2><p>RTL مخفف Right-to-Left است. زبان‌هایی مثل فارسی و عربی از این نوع نگارش استفاده می‌کنند.</p>"
            }
        ]
        
        # Add blog posts
        created_count = 0
        for i, post_data in enumerate(sample_posts):
            if not BlogPage.objects.filter(title=post_data["title"]).exists():
                blog_post = blog_index.add_child(instance=BlogPage(
                    title=post_data["title"],
                    slug=f"blog-post-{i+1}",
                    intro=post_data["intro"],
                    body=post_data["body"],
                    live=True
                ))
                self.stdout.write(self.style.SUCCESS(f'✓ Blog post {i+1} created: {blog_post.title}'))
                created_count += 1
            else:
                self.stdout.write(self.style.WARNING(f'✓ Blog post "{post_data["title"]}" already exists'))
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Completed! {created_count} new posts created.'))
