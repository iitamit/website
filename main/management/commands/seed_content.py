from django.core.management.base import BaseCommand

from main.models import ChartEntry, Drama, FashionLook, SiteSettings, Story, Video


class Command(BaseCommand):
    help = "Populate an empty IK Seoul database with starter content."

    def handle(self, *args, **options):
        settings = SiteSettings.load()
        if not settings.breaking_news:
            settings.breaking_news = (
                "BTS 2026 Full Comeback Confirmed - All 7 Members Together Again || "
                'Stray Kids "MIROH" World Tour - India Dates Announced || '
                "aespa Wins MAMA 2026 Best Female Group Daesang"
            )
            settings.ticker_items = (
                'Jennie "Ruby" Sequel Drops April 2026 || '
                "ARMY India Fan Fest 2026 - Hyderabad March 22 || "
                "aespa Supernova MV Crosses 1B Views"
            )
            settings.award_title = "BTS Win Daesang - Artist of the Year at MAMA 2026"
            settings.award_meta = "December 2026 - Ceremony held in Tokyo"
            settings.award_bullets = (
                "Best Male Group - SEVENTEEN || Best Female Group - aespa || "
                "Best New Artist - BABYMONSTER"
            )
            settings.save()

        Story.objects.get_or_create(
            title="All 7 Members Reunite: BTS 2026 Full Comeback Is Finally Here",
            defaults={
                "category": "BTS x India - Editor's Pick",
                "read_time": "14 min read",
                "excerpt": "All seven members have officially confirmed their full-group comeback.",
                "emoji": "BTS",
                "tags": "BTS, 2026 Comeback, India",
                "featured": True,
            },
        )
        FashionLook.objects.get_or_create(
            artist="V (BTS)",
            title="Celine Oversized Wool Coat",
            defaults={
                "brand": "Celine Paris - Winter 2026",
                "badge": "Viral",
                "emoji": "V",
                "description": "A structured oversized charcoal wool coat styled for a runway moment.",
                "shop_text": "Shop at Celine.com",
                "shop_url": "https://www.celine.com",
            },
        )
        ChartEntry.objects.get_or_create(
            chart=ChartEntry.SPOTIFY,
            rank=1,
            defaults={
                "title": "Yet To Come (2026 Remaster)",
                "artist": "BTS",
                "stat": "Up 1 - 42M",
                "emoji": "BTS",
                "meter": 95,
            },
        )
        Video.objects.get_or_create(
            youtube_id="BVwAVbKYYeM",
            defaults={
                "category": "BTS - Comeback",
                "title": "Dynamite - Comeback Stage",
                "meta": "All 7 Members - #1 Worldwide",
            },
        )
        Drama.objects.get_or_create(
            title="When the Stars Gossip S2",
            defaults={
                "meta": "Netflix - Space Romance",
                "status": "Airing Now",
                "emoji": "TV",
            },
        )
        self.stdout.write(self.style.SUCCESS("Starter content is ready."))
