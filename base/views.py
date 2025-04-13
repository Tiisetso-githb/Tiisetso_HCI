from django.shortcuts import render, redirect
from .forms import ReminderForm
from .models import Reminder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    reminders = Reminder.objects.all()
    return render(request, 'home.html', {'reminders': reminders})


##@login_required
##def create_reminder(request):
    ##return render(request, "create_reminder.html", {})

def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    else:
        form = ReminderForm()
    return render(request, 'registration/create_reminder.html', {'form': form})



def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})
