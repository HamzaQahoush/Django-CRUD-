from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Hamza ", email="hamza.qah@gmail.com", password="pwd"
        )

        self.snack = Snack.objects.create(
            title="Banana juice with milk",
            purchaser=self.user,
            description="Banana juice with milk is tasy drink",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Banana juice with milk")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Banana juice with milk")
        self.assertEqual(f"{self.snack.purchaser}", "Hamza ")
        self.assertEqual(
            self.snack.description,
            "Banana juice with milk is tasy drink",
        )

    def test_snack_list_view(self):
        response = self.client.get(reverse("view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Banana juice with milk")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("detailView", args="1"))
        no_response = self.client.get("/8000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Banana",
                "purchaser": self.user.id,
                "description": "good snack",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("detailView", args="2"))
        self.assertContains(response, "Banana")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {
                "title": "Updated title",
                "purchaser": self.user.id,
                "description": "New description",
            },
        )

        self.assertRedirects(response, reverse("detailView", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)
