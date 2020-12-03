from django.urls import path
from author import views

app_name = 'author'

urlpatterns = [
    path('author', views.AuthorApi.as_view()),
    path(
            'author/create',
            views.AuthorCreateApi.as_view(),
            name='create'
        )
]
