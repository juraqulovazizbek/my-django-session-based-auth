from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView

from .forms import CustomUserCreationForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomLogoutView(LogoutView):
    pass


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/profile.html')

