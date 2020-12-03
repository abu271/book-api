from django.urls import path
from book import views

app_name = 'book'

urlpatterns = [
    path('book', views.BookApi.as_view()),
    path(
            'book/create',
            views.BookCreateApi.as_view(),
            name='create'
        )
]
