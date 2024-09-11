from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.http import Http404
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


@login_required
def update(request, pk):
    pomodoro = pomodoro_belongs_to_user_or_404(request.user, pk)
    if request.method == "POST":
        form = PomodoroForm(request.POST, instance=pomodoro)

        if form.is_valid():
            form.save()
            return redirect("pomodoros:index")
    else:
        form = PomodoroForm(instance=pomodoro)
    return render(request, "pomodoros/update.html", {"form": form, "pomodoro_id": pk})


@login_required
def delete(request, pk):
    pomodoro = pomodoro_belongs_to_user_or_404(request.user, pk)
    pomodoro.delete()
    return redirect("pomodoros:index")


def pomodoro_belongs_to_user_or_404(user, pk):
    pomodoro = get_object_or_404(Pomodoro, pk=pk)

    if pomodoro.user.id != user.id:
        raise Http404
    return pomodoro
