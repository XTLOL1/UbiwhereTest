from django.contrib.auth.models import Group, User
from rest_framework import serializers
from restapp.models import RoadSegment, SegmentSpeed, SpeedTier

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RoadSegmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoadSegment
        fields = ['url', 'longStartId', 'latStartId', 'longEndId', 'latEndId', 'length']

class SegmentSpeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SegmentSpeed
        fields = ['url', 'roadSegment', 'dateTimeUpdated', 'speed']

class SpeedTierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpeedTier
        fields = ['url', 'lowerLimit', 'upperLimit', 'designation']
