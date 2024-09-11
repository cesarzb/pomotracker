from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Pomodoro
from .forms import PomodoroForm


@login_required
def index(request):
    pomodoros = Pomodoro.objects.filter(user=request.user).order_by("-end_date")
    return render(request, "pomodoros/index.html", {"pomodoros": pomodoros})


@login_required
def create(request):
    if request.method == "POST":
        form = PomodoroForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("pomodoros:index")
    else:
        form = PomodoroForm(
            initial={"start_date": timezone.now(), "end_date": timezone.now()}
        )
    return render(request, "pomodoros/create.html", {"form": form})
