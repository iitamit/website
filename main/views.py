from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import (
    ChartEntry,
    Drama,
    FashionLook,
    NewsletterSubscriber,
    SiteSettings,
    Story,
    Video,
)


def _items(value):
    return [item.strip() for item in value.split("||") if item.strip()]


def index(request):
    settings = SiteSettings.load()
    videos = Video.objects.filter(active=True)
    return render(
        request,
        "main/index.html",
        {
            "site_settings": settings,
            "breaking_news": _items(settings.breaking_news),
            "ticker_items": _items(settings.ticker_items),
            "award_bullets": _items(settings.award_bullets),
            "stories": Story.objects.filter(published=True),
            "fashion_looks": FashionLook.objects.filter(active=True),
            "spotify_entries": ChartEntry.objects.filter(chart=ChartEntry.SPOTIFY),
            "billboard_entries": ChartEntry.objects.filter(chart=ChartEntry.BILLBOARD),
            "videos": videos,
            "featured_video": videos.first(),
            "dramas": Drama.objects.filter(active=True),
        },
    )


@require_POST
def subscribe(request):
    email = request.POST.get("email", "").strip().lower()
    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"ok": False, "error": "Enter an email address."}, status=400)
    subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
    return JsonResponse({"ok": True, "created": created, "email": subscriber.email})
