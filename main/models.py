from django.db import models


class SiteSettings(models.Model):
    breaking_news = models.TextField(blank=True)
    ticker_items = models.TextField(blank=True)
    award_title = models.CharField(max_length=255, blank=True)
    award_meta = models.CharField(max_length=255, blank=True)
    award_bullets = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "site settings"

    @classmethod
    def load(cls):
        settings, _ = cls.objects.get_or_create(pk=1)
        return settings


class Story(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=120)
    read_time = models.CharField(max_length=40, default="5 min read")
    excerpt = models.TextField()
    emoji = models.CharField(max_length=20, blank=True)
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    @property
    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]

    def __str__(self):
        return self.title


class FashionLook(models.Model):
    artist = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    badge = models.CharField(max_length=60, blank=True)
    emoji = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    shop_text = models.CharField(max_length=120, blank=True)
    shop_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.artist} - {self.title}"


class ChartEntry(models.Model):
    SPOTIFY = "spotify"
    BILLBOARD = "billboard"
    CHART_CHOICES = [(SPOTIFY, "Spotify"), (BILLBOARD, "Billboard")]

    chart = models.CharField(max_length=20, choices=CHART_CHOICES)
    rank = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=120)
    stat = models.CharField(max_length=80, blank=True)
    emoji = models.CharField(max_length=20, blank=True)
    meter = models.PositiveSmallIntegerField(default=50)

    class Meta:
        ordering = ["chart", "rank"]

    def __str__(self):
        return f"{self.chart}: #{self.rank} {self.title}"


class Video(models.Model):
    youtube_id = models.CharField(max_length=32)
    category = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    meta = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Drama(models.Model):
    title = models.CharField(max_length=255)
    meta = models.CharField(max_length=255)
    status = models.CharField(max_length=60)
    emoji = models.CharField(max_length=20, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
