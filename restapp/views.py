from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, views, response

from restapp.serializers import GroupSerializer, UserSerializer, RoadSegmentSerializer, SegmentSpeedSerializer, SpeedTierSerializer
import restapp.models as restModels

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

class RoadSegmentViewSet(viewsets.ModelViewSet):
    queryset = restModels.RoadSegment.objects.all().order_by('id')
    serializer_class = RoadSegmentSerializer

class SegmentSpeedViewSet(viewsets.ModelViewSet):
    queryset = restModels.SegmentSpeed.objects.all().order_by('id')
    serializer_class = SegmentSpeedSerializer

class SpeedTierViewSet(viewsets.ModelViewSet):
    queryset = restModels.SpeedTier.objects.all()
    serializer_class = SpeedTierSerializer
