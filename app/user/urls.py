from rest_framework.routers import DefaultRouter
from django.urls import path, include
from user import views

app_name = 'user'

router = DefaultRouter()
router.register('users', views.UserViewSet, app_name)


urlpatterns = [
  path('', include((router.urls)))
]
