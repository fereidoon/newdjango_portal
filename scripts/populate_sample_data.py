#!/usr/bin/env python
"""
Script to populate the database with sample Persian content
Run with: python manage.py shell < scripts/populate_sample_data.py
"""

from django.utils import timezone
from wagtail.models import Page
from apps.home.models import HomePage, BlogIndexPage, BlogPage

def populate_sample_data():
    print("🚀 Starting to populate sample data...")
    
    # Get or create the root page
    try:
        root_page = Page.objects.get(depth=1)
    except Page.DoesNotExist:
        print("❌ Root page not found!")
        return
    
    # Create Home Page if it doesn't exist
    if not HomePage.objects.exists():
        home_page = HomePage.objects.create(
            title="صفحه اصلی",
            slug="home",
            intro="<p>خوش آمدید به پورتال ما! این یک مرکز مدیریت محتوا است که بر پایه Django و Wagtail بنا شده است.</p>",
            live=True,
            parent=root_page
        )
        print(f"✓ Home page created: {home_page.title}")
    else:
        home_page = HomePage.objects.first()\n        print(f"✓ Home page already exists: {home_page.title}")
    
    # Create Blog Index Page if it doesn't exist
    if not BlogIndexPage.objects.exists():
        blog_index = BlogIndexPage.objects.create(
            title="وبلاگ",
            slug="blog",
            intro="<p>آخرین مقالات و نوشته های ما را اینجا بخوانید.</p>",
            live=True,
            parent=root_page
        )
        print(f"✓ Blog index page created: {blog_index.title}")
    else:
        blog_index = BlogIndexPage.objects.first()
        print(f"✓ Blog index page already exists: {blog_index.title}")
    
    # Create sample blog posts
    sample_posts = [
        {
            "title": "آغاز یک سفر جدید به دنیای وب",
            "intro": "در این مقاله، ما درباره آخرین تکنولوژی‌های وب صحبت خواهیم کرد.",
            "body": "<h2>مقدمه</h2><p>وب با سرعت زیادی درحال تکامل است. هر روز تکنولوژی‌های جدیدی معرفی می‌شوند که به ما کمک می‌کنند بهتر کار کنیم. در این مقاله، ما سعی می‌کنیم برخی از مهم‌ترین این تکنولوژی‌ها را بررسی کنیم.</p><h2>اهمیت Django</h2><p>Django یکی از بهترین فریم‌ورک‌های Python برای توسعه وب است. این فریم‌ورک به ما کمک می‌کند تا web application‌های امن و مقیاس‌پذیر بسازیم.</p>"
        },
        {
            "title": "محتوای بهتر با Wagtail CMS",
            "intro": "Wagtail یکی از بهترین سیستم‌های مدیریت محتوا برای Django است.",
            "body": "<h2>چرا Wagtail؟</h2><p>Wagtail بسیار قدرتمند است و استفاده از آن بسیار آسان. شما می‌توانید صفحات پیچیده‌ای را بدون نوشتن کد بیشتر درست کنید.</p><p>یکی دیگر از مزایای Wagtail، واسط کاربری آن است که بسیار کاربرپسند و جدید است.</p>"
        },
        {
            "title": "طراحی شامل و مناسب برای تمام برنامه‌ها",
            "intro": "در عصر دیجیتالی، داشتن یک وب‌سایت پاسخگو بسیار ضروری است.",
            "body": "<h2>اهمیت طراحی واکنش‌پذیر</h2><p>امروزه، اکثر کاربران از تلفن‌های هوشمند برای دسترسی به وب‌سایت‌ها استفاده می‌کنند. بنابراین، داشتن یک طراحی واکنش‌پذیر نه تنها اختیاری است، بلکه ضروری است.</p><p>ما در این پروژه، Bootstrap 5 را استفاده کردیم تا اطمینان حاصل کنیم که وب‌سایت از تمامی دستگاه‌ها به خوبی دیده می‌شود.</p>"
        },
        {
            "title": "پشتیبانی کامل فارسی و RTL",
            "intro": "یکی از ویژگی‌های خاص این پرژه، پشتیبانی کامل زبان فارسی و نگارش راست‌چپ است.",
            "body": "<h2>چرا فارسی؟</h2><p>فارسی یکی از زبان‌های مهم است. و این پروژه به طور کامل برای استفاده با زبان فارسی طراحی شده است.</p><h2>RTL چیست؟</h2><p>RTL مخفف Right-to-Left است. یعنی نگارش از راست به چپ. زبان‌هایی مثل فارسی، عربی، و عبری از این نوع نگارش استفاده می‌کنند و ما از CSS RTL برای پشتیبانی آن استفاده کردیم.</p>"
        }
    ]
    
    # Add blog posts
    for i, post_data in enumerate(sample_posts):
        if not BlogPage.objects.filter(title=post_data["title"]).exists():
            blog_post = BlogPage.objects.create(
                title=post_data["title"],
                slug=post_data["title"].lower().replace(" ", "-"),
                intro=post_data["intro"],
                body=post_data["body"],
                live=True,
                parent=blog_index
            )
            print(f"✓ Blog post {i+1} created: {blog_post.title}")
        else:
            print(f"✓ Blog post '{post_data['title']}' already exists")
    
    print("\n✅ Sample data population completed!")

if __name__ == "__main__":
    populate_sample_data()
