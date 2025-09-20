from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, views, response

from restapp.serializers import GroupSerializer, UserSerializer, RoadSegmentSerializer, SegmentSpeedSerializer, SpeedTierSerializer, RoadSegmentWithSpeedsSerializer
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

class FindRoadSegment(views.APIView):
    serializer_class = RoadSegmentWithSpeedsSerializer
    #this will only run if every parameter is present
    def get(self, request, *args, **kwargs):
        startLong = self.kwargs["startLong"]
        startLat = self.kwargs["startLat"]
        endLong = self.kwargs["endLong"]
        endLat = self.kwargs["endLat"]
        roadSegment = restModels.RoadSegment.objects.filter(
            longStartId=startLong,
            latStartId=startLat,
            longEndId=endLong,
            latEndId=endLat
        )[0]
        if roadSegment is not None:
            serializer = RoadSegmentWithSpeedsSerializer(roadSegment, context={'request': request})
            return response.Response(serializer.data)
        else:
            return response.Response(status=404)
        
class RoadSegmentsByLastSpeedReadingDesignation(views.APIView):
    serializer_class = RoadSegmentSerializer

    #only runs if designation is present
    def get(self, request, designation):
        #designation = self.kwargs["designation"]
        speedTier = restModels.SpeedTier.objects.filter(designation=designation)
        if not speedTier.exists():
            return response.Response({"status": "designation doesn't exist"}, status=404)
        speedTier = speedTier[0]
        roads = restModels.RoadSegment.objects.all()
        returnList = []
        for road in roads:
            mostRecentSpeedReading = restModels.SegmentSpeed.objects.filter(roadSegment=road).latest("dateTimeUpdated")
            if speedTier.lowerLimit is None:
                #-infinite to upperLimit
                if mostRecentSpeedReading.speed <= speedTier.upperLimit:
                    returnList.append(road)
            elif speedTier.upperLimit is None:
                #lowerLimit to infinite
                if mostRecentSpeedReading.speed > speedTier.lowerLimit:
                    returnList.append(road)
            else:
                #lowerLimit to upperLimit
                if mostRecentSpeedTier.speed <= speedTier.upperLimit and object.speed > speedTier.lowerLimit:
                    returnList.append(road)
            
        if not returnList: #empty
            return response.Response(status=204)
        else:
            return response.Response(RoadSegmentSerializer(returnList, many=True, context={'request': request}).data)
