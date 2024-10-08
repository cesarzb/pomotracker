from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import TruncDate
from collections import defaultdict

class Pomodoro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    finished = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.start_date.strftime("%d %b %Y")
