from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.models import ChartEntry, Drama, FashionLook, SiteSettings, Story, Video


def _field(request, name, default=""):
    return request.POST.get(name, default).strip()


@login_required
def index(request):
    return render(
        request,
        "dashboard/index.html",
        {
            "site_settings": SiteSettings.load(),
            "stories": Story.objects.all(),
            "fashion_looks": FashionLook.objects.all(),
            "spotify_entries": ChartEntry.objects.filter(chart=ChartEntry.SPOTIFY),
            "billboard_entries": ChartEntry.objects.filter(chart=ChartEntry.BILLBOARD),
            "videos": Video.objects.all(),
            "dramas": Drama.objects.all(),
        },
    )


@login_required
@require_POST
def save_settings(request):
    settings = SiteSettings.load()
    settings.breaking_news = _field(request, "breaking_news", settings.breaking_news)
    settings.ticker_items = _field(request, "ticker_items", settings.ticker_items)
    settings.award_title = _field(request, "award_title", settings.award_title)
    settings.award_meta = _field(request, "award_meta", settings.award_meta)
    settings.award_bullets = _field(request, "award_bullets", settings.award_bullets)
    settings.save()
    messages.success(request, "Site settings saved.")
    return redirect("dashboard:index")


@login_required
@require_POST
def add_story(request):
    Story.objects.create(
        title=_field(request, "title"),
        category=_field(request, "category"),
        read_time=_field(request, "read_time", "5 min read"),
        excerpt=_field(request, "excerpt"),
        emoji=_field(request, "emoji"),
        tags=_field(request, "tags"),
        featured=request.POST.get("featured") == "on",
    )
    messages.success(request, "Story published.")
    return redirect("dashboard:index")


@login_required
@require_POST
def add_fashion_look(request):
    FashionLook.objects.create(
        artist=_field(request, "artist"),
        title=_field(request, "title"),
        brand=_field(request, "brand"),
        badge=_field(request, "badge"),
        emoji=_field(request, "emoji"),
        description=_field(request, "description"),
        shop_text=_field(request, "shop_text"),
        shop_url=_field(request, "shop_url"),
    )
    messages.success(request, "Runway look added.")
    return redirect("dashboard:index")


@login_required
@require_POST
def add_chart_entry(request):
    chart = _field(request, "chart")
    if chart not in {ChartEntry.SPOTIFY, ChartEntry.BILLBOARD}:
        raise Http404
    ChartEntry.objects.create(
        chart=chart,
        rank=request.POST.get("rank", 1),
        title=_field(request, "title"),
        artist=_field(request, "artist"),
        stat=_field(request, "stat"),
        emoji=_field(request, "emoji"),
        meter=request.POST.get("meter", 50),
    )
    messages.success(request, "Chart entry added.")
    return redirect("dashboard:index")


@login_required
@require_POST
def add_video(request):
    Video.objects.create(
        youtube_id=_field(request, "youtube_id"),
        category=_field(request, "category"),
        title=_field(request, "title"),
        meta=_field(request, "meta"),
    )
    messages.success(request, "Video added.")
    return redirect("dashboard:index")


@login_required
@require_POST
def add_drama(request):
    Drama.objects.create(
        title=_field(request, "title"),
        meta=_field(request, "meta"),
        status=_field(request, "status"),
        emoji=_field(request, "emoji"),
    )
    messages.success(request, "Drama added.")
    return redirect("dashboard:index")


MODEL_MAP = {
    "story": Story,
    "fashion": FashionLook,
    "chart": ChartEntry,
    "video": Video,
    "drama": Drama,
}


@login_required
@require_POST
def delete_item(request, model_name, pk):
    model = MODEL_MAP.get(model_name)
    if model is None:
        raise Http404
    get_object_or_404(model, pk=pk).delete()
    messages.success(request, "Item deleted.")
    return redirect("dashboard:index")
