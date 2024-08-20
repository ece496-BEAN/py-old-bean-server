from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from beanserver.beanapi.serializers import GroupSerializer
from beanserver.beanapi.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet[User]):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet[Group]):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
