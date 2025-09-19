from django.urls import path, include
from rest_framework import routers
from restapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'roadSegments', views.RoadSegmentViewSet)
router.register(r'segmentSpeeds', views.SegmentSpeedViewSet)
router.register(r'SpeedTierViewSet', views.SpeedTierViewSet)

urlpatterns = [
    path('', include(router.urls))
]
