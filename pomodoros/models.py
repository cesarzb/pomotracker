from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import TruncDate
from collections import defaultdict


class PomodoroManager(models.Manager):
    def grouped_by_day(self, user):
        qs = (
            self.get_queryset()
            .filter(user=user)
            .annotate(date=TruncDate("end_date"))
            .order_by("date")
        )

        grouped_pomodoros = defaultdict(list)
        for pomodoro in qs:
            grouped_pomodoros[pomodoro.date].append(pomodoro)

        return dict(grouped_pomodoros)


class Pomodoro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    finished = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    objects = PomodoroManager()

    def __str__(self):
        return self.start_date.strftime("%d %b %Y")
