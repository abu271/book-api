from rest_framework.routers import DefaultRouter
from django.urls import path, include
from book import views


router = DefaultRouter()
router.register("books", views.BookViewSet)

app_name = 'book'


urlpatterns = [
    path('', include((router.urls)))
]
