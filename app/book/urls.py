from django.urls import path
from .views import book_views

app_name = 'book'

urlpatterns = [
    path('book', book_views.BookApi.as_view()),
    path(
            'book/create',
            book_views.BookCreateApi.as_view(),
            name='create'
        )
]
