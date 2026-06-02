from django.test import TestCase
from django.urls import reverse

from .models import NewsletterSubscriber, Story


class PublicSiteTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("main:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Queen of Tears S2")
        self.assertContains(response, "Mingyu (SEVENTEEN)")

    def test_newsletter_signup_is_persisted(self):
        response = self.client.post(reverse("main:subscribe"), {"email": "fan@example.com"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(NewsletterSubscriber.objects.filter(email="fan@example.com").exists())

    def test_newsletter_signup_rejects_invalid_email(self):
        response = self.client.post(reverse("main:subscribe"), {"email": "not-an-email"})
        self.assertEqual(response.status_code, 400)

    def test_favicon_request_is_handled(self):
        response = self.client.get("/favicon.ico")
        self.assertEqual(response.status_code, 204)


class DashboardTests(TestCase):
    def test_dashboard_is_available_without_admin_login(self):
        response = self.client.get(reverse("dashboard:index"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_subdomain_root_redirects_to_dashboard(self):
        response = self.client.get("/", HTTP_HOST="dash.localhost")
        self.assertRedirects(
            response,
            reverse("dashboard:index"),
            fetch_redirect_response=False,
        )

    def test_dashboard_can_publish_story_to_public_site(self):
        response = self.client.post(
            reverse("dashboard:add_story"),
            {
                "title": "A new story",
                "category": "News",
                "read_time": "3 min read",
                "excerpt": "A useful summary.",
            },
        )
        self.assertRedirects(response, reverse("dashboard:index"))
        self.assertTrue(Story.objects.filter(title="A new story").exists())
        public_response = self.client.get(reverse("main:index"))
        self.assertContains(public_response, "A new story")
