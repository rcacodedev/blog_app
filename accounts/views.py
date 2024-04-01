"""
Views for the accounts app.
"""

from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import CustomUser

class RegisterView(SuccessMessageMixin, CreateView):
    """
    View for the registration of a new user.
    """
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    success_message = 'Account created successfully.'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class LoginView(SuccessMessageMixin, LoginView):
    """
    View for the login of an existing user.
    """
    model = CustomUser
    template_name = 'accounts/login.html'
    success_message = 'Login successful.'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog_app:home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)