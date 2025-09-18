from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, views, response

from djangoapp.ubiwheretest.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer

class RoadSegments(views.APIView):
    pass

class StreetSpeeds(views.APIView):
    def get(self, request, format=None):
	    pass
