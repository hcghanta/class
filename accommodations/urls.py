from django.urls import path
from . import views

app_name = 'accommodations'

urlpatterns = [
    path('', views.accommodation_list, name='accommodation_list'),
    path('<slug:category_slug>/', views.accommodation_list,
         name='accommodation_list_by_category'),
    path('<int:id>/<slug:slug>/', views.accommodation_detail,
         name='accommodation_detail'),
]

