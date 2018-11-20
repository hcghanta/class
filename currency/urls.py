from django.urls import path
from .import views


app_name = 'currency'

urlpatterns = [
    path('', views.index, name='currency_list'),
    path('currency_list/', views.test, name='currency_table'),
    path('currency/<int:pk>/delete', views.currency_delete, name='currency_delete'),
]