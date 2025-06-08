from rest_framework.routers import DefaultRouter
from django.urls import path, include
from author import views

app_name = 'author'

router = DefaultRouter()
router.register('authors', views.AuthorViewSet, app_name)

urlpatterns = [
    path('', include((router.urls)))
]
