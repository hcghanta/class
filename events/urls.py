from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('register_event/', views.event_new, name='event_new'),
    path('<slug:category_slug>/', views.event_list,
         name='event_list_by_category'),
    path('<int:id>/<slug:slug>/', views.event_detail,
         name='event_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
