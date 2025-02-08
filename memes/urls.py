from django.urls import path
from . import views

urlpatterns = [
    path('', views.meme_list, name='meme_list'),
]