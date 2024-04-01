"""
Urls for the accounts app.
"""

from django.urls import path
from .views import RegisterView, LoginView

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('accounts:login')), name='logout'),
]