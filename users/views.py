from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, LogoutView
from django.views import View
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator

from .forms import CustomUserCreationForm, LoginForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(View):
    def get(self,  request: HttpRequest) -> HttpResponse:
        form = LoginForm
        return render(request, 'users/login.html', {'form': form})
    
    def post(self,  request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('profile'))

        return render(request, 'users/login.html', {'form': form})
    

class CustomLogoutView(LogoutView):
    pass


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    user = request.user
    tasks = user.tasks.all()
    return render(request, 'users/profile.html', {"user": user, "tasks": tasks})

@method_decorator(login_required, name="dispatch")
class CreateTaskView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        pass

    def post(self, request: HttpRequest) -> HttpResponse:
        pass