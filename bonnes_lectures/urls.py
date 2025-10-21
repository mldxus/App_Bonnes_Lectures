from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'), 
    path('about/', views.about, name='about'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('book/', views.book_summary_list, name='book-summary-list'),
    path('new_book/', views.book_create, name='book-create'),
    path('book/<int:pk>/delete/', views.book_delete, name='book-delete'),
    path('book/<int:pk>/edit/', views.book_update, name='book-update'),
]

