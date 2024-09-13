import datetime
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class PomodoroTests(TestCase):
    def create_and_log_in_user(self, name="Peter"):
        user = User.objects.create_user(name, f"{name}@guardians.com", "Password123$")
        self.client.force_login(user)
        return user

    def create_pomodoro_for_user(self, user, minutes):
        end_time = timezone.now() - datetime.timedelta(minutes=minutes)
        start_time = end_time - datetime.timedelta(minutes=25)
        pomodoro = user.pomodoro_set.create(
            start_date=start_time, end_date=end_time, finished=True
        )
        return pomodoro

    # CREATE
    def test_creating_post_works(self):
        """
        This test will check if user can successfully create a pomodoro
        """
        user = self.create_and_log_in_user()
        end_date = timezone.now() - datetime.timedelta(minutes=12)
        start_date = end_date - datetime.timedelta(minutes=25)

        response = self.client.post(
            reverse("pomodoros:create"),
            {
                "start_date": start_date,
                "end_date": end_date,
                "finished": True,
            },
        )
        self.assertRedirects(
            response,
            reverse("pomodoros:index"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        pomodoro = user.pomodoro_set.all()[0]
        self.assertEqual(pomodoro.start_date, start_date)
        self.assertEqual(pomodoro.end_date, end_date)
        self.assertEqual(pomodoro.finished, True)

    # READ
    def test_user_can_list_his_pomodoros(self):
        """
        This test will check if user's pomodoros are shown in index view
        """
        user = self.create_and_log_in_user()
        pomodoro1 = self.create_pomodoro_for_user(user, 37)
        pomodoro2 = self.create_pomodoro_for_user(user, 1544)

        calendar_pomodoros = [
        {
            'title': 'Pomodoro',
            'start': pomodoro.start_date.isoformat(),
            'end': pomodoro.end_date.isoformat(),
            'url': reverse('pomodoros:show', args=[pomodoro.id])
        }
        for pomodoro in [pomodoro1, pomodoro2]
    ]

        response = self.client.get(reverse("pomodoros:index"))
        self.assertEquals(response.status_code, 200)
        self.assertQuerySetEqual(response.context["calendar_pomodoros"], calendar_pomodoros)

    # UPDATE
    def test_user_can_update_his_pomodoro(self):
        """
        This test will check if user can successfully update his pomodoro
        """
        user = self.create_and_log_in_user()
        pomodoro = self.create_pomodoro_for_user(user, 37)
        new_start_date = pomodoro.start_date - datetime.timedelta(minutes=42)
        new_end_date = pomodoro.end_date - datetime.timedelta(minutes=42)

        response = self.client.post(
            reverse("pomodoros:update", args=[pomodoro.id]),
            {
                "start_date": new_start_date,
                "end_date": new_end_date,
                "finished": False,
            },
        )
        self.assertRedirects(
            response,
            reverse("pomodoros:index"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        pomodoro.refresh_from_db()
        self.assertEqual(pomodoro.start_date, new_start_date)
        self.assertEqual(pomodoro.end_date, new_end_date)
        self.assertEqual(pomodoro.finished, False)

    # DELETE
    def test_test_deleting_post_works(self):
        user = self.create_and_log_in_user()
        pomodoro = self.create_pomodoro_for_user(user, 37)
        response = self.client.post(
            reverse("pomodoros:delete", args=[pomodoro.id]),
        )
        self.assertRedirects(
            response,
            reverse("pomodoros:index"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertQuerySetEqual(user.pomodoro_set.all(), [])

    # FOR OTHER USER

    # INDEX
    def test_user_cannot_list_someones_pomodoros(self):
        """
        This test will check if user can only list his pomodoros
        """
        user = self.create_and_log_in_user()
        self.client.logout()
        self.create_pomodoro_for_user(user, 37)
        other_user = self.create_and_log_in_user("Parker")
        pomodoro2 = self.create_pomodoro_for_user(other_user, 1485)
        pomodoro3 = self.create_pomodoro_for_user(other_user, 12)

        calendar_pomodoros = [
        {
            'title': 'Pomodoro',
            'start': pomodoro.start_date.isoformat(),
            'end': pomodoro.end_date.isoformat(),
            'url': reverse('pomodoros:show', args=[pomodoro.id])
        }
        for pomodoro in [pomodoro2, pomodoro3]
        ]

        response = self.client.get(reverse("pomodoros:index"))
        self.assertEquals(response.status_code, 200)
        self.assertQuerySetEqual(response.context["calendar_pomodoros"], calendar_pomodoros)
    
    # SHOW
    def test_user_cannot_see_someones_pomodoro(self):
            """
            This test will check if user cannot see somoeone's pomodoro
            """
            user = self.create_and_log_in_user()
            self.client.logout()
            pomodoro = self.create_pomodoro_for_user(user, 37)
            self.create_and_log_in_user("Parker")

            response = self.client.post(
                reverse("pomodoros:show", args=[pomodoro.id]),
            )
            self.assertEqual(response.status_code, 404)

    # UPDATE
    def test_user_cannot_update_someones_pomodoro(self):
        """
        This test will check if user cannot update someone's pomodoro
        """
        user = self.create_and_log_in_user()
        self.client.logout()
        pomodoro = self.create_pomodoro_for_user(user, 37)
        self.create_and_log_in_user("Parker")

        response = self.client.post(
            reverse("pomodoros:update", args=[pomodoro.id]),
        )
        self.assertEqual(response.status_code, 404)

    # DELETE
    def test_user_cannot_delete_someones_pomodoro(self):
        """
        This test will check if user cannot delete someone's pomodoro
        """
        user = self.create_and_log_in_user()
        self.client.logout()
        pomodoro = self.create_pomodoro_for_user(user, 37)
        self.create_and_log_in_user("Parker")

        response = self.client.post(
            reverse("pomodoros:delete", args=[pomodoro.id]),
        )
        self.assertEqual(response.status_code, 404)
