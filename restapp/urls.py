from django.urls import path, re_path, include
from rest_framework import routers
from restapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'roadSegments', views.RoadSegmentViewSet)
router.register(r'segmentSpeeds', views.SegmentSpeedViewSet)
router.register(r'speedTiers', views.SpeedTierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'findRoadSegment/(?P<startLong>[-+]?([0-9]+\.[0-9]+|[0-9]+))/(?P<startLat>[-+]?([0-9]+\.[0-9]+|[0-9]+))/(?P<endLong>[-+]?([0-9]+\.[0-9]+|[0-9]+))/(?P<endLat>[-+]?([0-9]+\.[0-9]+|[0-9]+))/', views.FindRoadSegment.as_view()),
    path('roadSegmentsByLastSpeedReadingDesignation/<str:designation>', views.RoadSegmentsByLastSpeedReadingDesignation.as_view()),
    #path('speedTier', views.SpeedTierViewSet.as_view({'get': 'list'}))
]
