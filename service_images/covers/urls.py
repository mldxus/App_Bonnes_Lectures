from django.urls import path
from . import views

urlpatterns = [
    path('api/<str:isbn>/', views.api_cover, name='api_cover'),
    path('gui/<str:isbn>/', views.gui_cover, name='gui_cover'),
]