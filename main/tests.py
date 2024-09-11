from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UserAuthTests(TestCase):

    def create_user(self):
        return User.objects.create_user("Peter", "quill@guardians.com", "Password123$")

    def test_user_can_login_with_correct_credentials(self):
        """
        For correct login data view will redirect to root and there return 200
        """
        self.create_user()
        response = self.client.post(
            reverse("login"),
            {"username": "Peter", "password": "Password123$"},
        )
        self.assertRedirects(
            response,
            reverse("main:home"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_user_cannot_login_with_incorrect_credentials(self):
        """
        For incorrect login data view will return 200 code and stay on page
        """
        self.create_user()
        response = self.client.post(
            reverse("login"),
            {"username": "Peter", "password": ""},
        )
        self.assertEqual(response.status_code, 200)

    def test_user_can_sign_up_with_correct_credentials(self):
        """
        For correct sign up data view will redirect to root and there return 200
        """
        response = self.client.post(
            reverse("main:sign_up"),
            {
                "username": "Peter",
                "email": "quill@guardians.com",
                "password1": "Password123$",
                "password2": "Password123$",
            },
        )
        self.assertRedirects(
            response,
            reverse("main:home"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_user_cannot_sing_up_with_incorrect_credentials(self):
        """
        For incorrect sign up data view will return 200 code and stay on the page
        """
        response = self.client.post(
            reverse("main:sign_up"),
            {
                "username": "Peter",
                "email": "quill@guardians.com",
                "password1": "password",
                "password2": "passw",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_home_page_requires_login(self):
        """
        Accessing home page without login will redirect to login
        """
        response = self.client.get(reverse("main:home"))
        self.assertRedirects(
            response,
            "/login?next=/",
            status_code=302,
            target_status_code=301,
            fetch_redirect_response=True,
        )

    def test_after_logout_user_has_to_login(self):
        self.create_user()
        self.client.post(
            reverse("login"),
            {"username": "Peter", "password": "Password123$"},
        )
        response = self.client.get(reverse("main:home"))
        self.assertEqual(response.status_code, 200)
        self.client.get(reverse("logout"))
        response = self.client.get(reverse("main:home"))
        self.assertRedirects(
            response,
            "/login?next=/",
            status_code=302,
            target_status_code=301,
            fetch_redirect_response=True,
        )
