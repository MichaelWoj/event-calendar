from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar_view'),
    path('', views.calendar_view, name='calendar_view'),
    path('event-detail/<int:event_id>/', views.event_detail_view, name='event_detail'),
]