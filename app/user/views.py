from rest_framework import viewsets
from core.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset for basic C.R.U.D operations
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
