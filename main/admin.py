from django.contrib import admin

from .models import (
    ChartEntry,
    Drama,
    FashionLook,
    NewsletterSubscriber,
    SiteSettings,
    Story,
    Video,
)

admin.site.register(
    [SiteSettings, Story, FashionLook, ChartEntry, Video, Drama, NewsletterSubscriber]
)
