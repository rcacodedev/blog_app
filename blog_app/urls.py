"""
Urls for the blog_app app.
"""

from django.urls import path
from .views import home, post_detail, cine, tv, videojuegos, literatura, podcasts

from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('post/<int:pk>/', post_detail.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('cine/', cine.as_view(), name='cine'),
    path('tv/', tv.as_view(), name='tv'),
    path('videojuegos/', videojuegos.as_view(), name='videojuegos'),
    path('literatura/', literatura.as_view(), name='literatura'),
    path('podcasts/', podcasts.as_view(), name='podcasts'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
]