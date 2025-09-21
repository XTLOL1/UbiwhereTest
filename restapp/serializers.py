from django.contrib.auth.models import Group, User
from rest_framework import serializers
from restapp.models import RoadSegment, SegmentSpeed, SpeedTier

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 
            'username', 
            'email', 
            'groups'
        ]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url', 
            'name'
        ]

class RoadSegmentSerializer(serializers.HyperlinkedModelSerializer):
    numSpeedReadings = serializers.SerializerMethodField()

    class Meta:
        model = RoadSegment
        fields = [
            'url', 
            'longStart', 
            'latStart', 
            'longEnd', 
            'latEnd', 
            'length', 
            'numSpeedReadings'
        ]

    def get_numSpeedReadings(self, object):
        return SegmentSpeed.objects.filter(roadSegment=object).count()

class SegmentSpeedSerializer(serializers.HyperlinkedModelSerializer):
    designation = serializers.SerializerMethodField()

    class Meta:
        model = SegmentSpeed
        fields = [
            'url', 
            'roadSegment', 
            'dateTimeUpdated', 
            'speed', 
            'designation'
        ]

    def get_designation(self, object):
        allSpeedTiers = SpeedTier.objects.all()
        for speedTier in allSpeedTiers:
            if speedTier.lowerLimit is None:
                #-infinite to upperLimit
                if object.speed <= speedTier.upperLimit:
                    return speedTier.designation
            elif speedTier.upperLimit is None:
                #lowerLimit to infinite
                if object.speed > speedTier.lowerLimit:
                    return speedTier.designation
            else:
                #lowerLimit to upperLimit
                if object.speed <= speedTier.upperLimit and object.speed > speedTier.lowerLimit:
                    return speedTier.designation
        return "Unknown" #failsafe

class RoadSegmentWithSpeedsSerializer(serializers.HyperlinkedModelSerializer):
    speedReadings = SegmentSpeedSerializer(many=True, read_only=True, source="segmentspeed_set")
    #same as fetch segspeeds where roadseg = x

    class Meta:
        model = RoadSegment
        fields = [
            'url',
            'length',
            'speedReadings'
        ]

class SpeedTierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpeedTier
        fields = [
            'url', 
            'lowerLimit', 
            'upperLimit', 
            'designation'
        ]
