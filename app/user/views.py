from rest_framework import viewsets
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset for basic C.R.U.D operations
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
