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
    path('book/<int:book_pk>/review/new/', views.review_create, name='review-create'),
    path('review/<int:pk>/update/', views.review_update, name='review-update'),
    path('review/<int:pk>/delete/', views.review_delete, name='review-delete'),
    path('authors/', views.author_list, name='author-list'),
    path('authors/new/', views.author_create, name='author-create'),
    path('authors/<int:pk>/update/', views.author_update, name='author-update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author-delete'),
    path('my-reviews/', views.my_review_list, name='my-review-list'),
]
