from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog_home"),              # home page
    path('about/', views.about, name="blog_about"),
]
