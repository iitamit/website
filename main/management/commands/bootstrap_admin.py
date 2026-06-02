import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create the first CMS administrator from CMS_ADMIN_* environment variables."

    def handle(self, *args, **options):
        username = os.environ.get("CMS_ADMIN_USERNAME", "admin")
        email = os.environ.get("CMS_ADMIN_EMAIL", "")
        password = os.environ.get("CMS_ADMIN_PASSWORD")
        if not password:
            raise CommandError("Set CMS_ADMIN_PASSWORD before running bootstrap_admin.")

        user, created = get_user_model().objects.get_or_create(
            username=username,
            defaults={"email": email, "is_staff": True, "is_superuser": True},
        )
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Created CMS administrator '{username}'."))
        else:
            self.stdout.write(f"CMS administrator '{username}' already exists.")
