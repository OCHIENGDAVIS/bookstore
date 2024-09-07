from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListVew.as_view(), name='book_list'),
    path('<uuid:pk>/', views.BookDetailView.as_view(), name='book_detail')
]
