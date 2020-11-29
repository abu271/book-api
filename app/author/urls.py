from django.urls import path
from .views import author_views

app_name = 'author'

urlpatterns = [
    path('author', author_views.AuthorApi.as_view()),
    path(
            'author/create',
            author_views.AuthorCreateApi.as_view(),
            name='create'
        )
]
