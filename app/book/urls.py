from rest_framework.routers import DefaultRouter
from django.urls import path, include
from book import views

app_name = 'book'

router = DefaultRouter()
router.register("books", views.BookViewSet, app_name)


urlpatterns = [
    path('', include((router.urls)))
]
