from django.urls import path
from .import views


app_name = 'sports'

urlpatterns = [
    path('', views.sport_list, name='sport_list'),
    path('cricket/', views.sport_cricket, name='sport_cricket'),
    path('nba/', views.sport_nba, name='sport_nba'),
]