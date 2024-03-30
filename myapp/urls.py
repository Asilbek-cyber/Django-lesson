# from django.contrib import admin
from django.urls import path

from .views import home_page, about_page, visit_page
urlpatterns = [
    path('home/', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('visit/', visit_page, name='visit'),
]
